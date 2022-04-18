import json
import typing
import uuid

import requests
from django.db.models import QuerySet
from django.db.transaction import atomic
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.utils import timezone
from rest_framework import serializers, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mroom import settings
from mroom.api.authentication.api import (
    PrivateAPIAuthentication,
    get_authorized_session
)
from mroom.api.email.campaign import Signup
from mroom.api.exceptions import (
    ServiceUnavailable,
    AuthenticationFailed,
)
from mroom.api.models import (
    User,
    Session,
    Appointment,
)
from mroom.api.serializer.appointment import AppointmentSerializer
from mroom.api.serializer.barber import BarberSerializer
from mroom.api.serializer.signin import SigninSerializer
from mroom.api.serializer.signup import SignupSerializer
from mroom.api.serializer.user import CurrentUserSerializer
from mroom.report.models import Survey


@api_view(['POST'])
@atomic
def signup(request: HttpRequest) -> JsonResponse:
    signup_data: typing.Dict = json.loads(request.body)

    serializer = SignupSerializer(data=signup_data)
    serializer.is_valid(raise_exception=True)

    terms: bool = serializer.data.get('terms')

    if terms == False:
        raise serializers.ValidationError(
            {
                'terms': [
                    'You must accept terms and conditions.'
                ]
            }
        )

    email: str = serializer.data.get('email')
    exists: bool = User.objects.filter(
        email=email,
    ).exists()

    if exists:
        raise serializers.ValidationError(
            {
                'email': [
                    'This email address is already being used.'
                ]
            }
        )

    user: User = User.objects.create_user(
        email=email,
        password=serializer.data.get('password'),
        name=serializer.data.get('name'),
        terms=serializer.data.get('terms')
    )
    user_survey = Survey.objects.get(
        key=Survey.DEFAULT,
        user__isnull=True,
    )

    user_survey.pk = None
    user_survey.id = None
    user_survey.uid = uuid.uuid4()
    user_survey.user = user
    user_survey.save()

    default_survey = Survey.objects.get(
        key=Survey.DEFAULT,
        user__isnull=True,
    )

    for question in default_survey.questions.all():
        user_survey.questions.add(question)

    try:
        response: requests.Response = requests.post(
            url=f'https://api.bigmailer.io/v1/brands'
                f'/{Signup.brand_id}/transactional-campaigns'
                f'/{Signup.campaign_id}/send',
            headers={
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-API-Key': settings.BIGMAILER_API_KEY
            },
            json={
                'email': user.email
            }
        )

        response.raise_for_status()
        sent: bool = True

    except Exception:
        sent: bool = False

    if not sent:
        raise ServiceUnavailable()
    return JsonResponse(
        status=201,
        data=CurrentUserSerializer(instance=user).data
    )



@api_view(['POST'])
def signin(request: HttpRequest) -> Response:
    signin_data: typing.Dict = json.loads(request.body)

    serializer = SigninSerializer(data=signin_data)
    serializer.is_valid(raise_exception=True)

    email: str = serializer.data.get('email')

    user_query: QuerySet = User.objects.filter(email=email)

    if not user_query.exists():
        raise AuthenticationFailed()

    user: User = user_query.first()

    if not user.check_password(
            raw_password=serializer.data.get('password')
    ):
        raise AuthenticationFailed()

    session: Session = Session.objects.create(user=user, is_active=True)

    response: Response = Response()
    response.set_cookie(
        key=settings.SESSION_COOKIE_NAME,
        expires=timezone.now() + settings.SESSION_DURATION,
        value=session.token,
        secure=True,
        httponly=True,
        samesite='Strict'
    )
    return response


@api_view(['POST'])
def signout(request: HttpRequest) -> Response:
    session: Session = get_authorized_session(
        request=request
    )

    session.last_active = timezone.now()
    session.is_active = False
    session.save()

    response: Response = Response()
    response.delete_cookie(
        settings.SESSION_COOKIE_NAME
    )

    return response


class CurrentUserViewSet(viewsets.ViewSet):
    authentication_classes = [PrivateAPIAuthentication]

    def list(self, request: HttpRequest) -> Response:
        return Response(
            CurrentUserSerializer(instance=request.user).data
        )


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class BarberViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_barber=True)
    serializer_class = BarberSerializer
