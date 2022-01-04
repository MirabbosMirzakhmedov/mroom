import json
import typing

import requests
from django.db.models import QuerySet
from django.db.transaction import atomic
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.utils import timezone
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mroom import settings
from mroom.api.authentication.api import PrivateAPIAuthentication
from mroom.api.authentication.api import get_authorized_session
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
from mroom.api.serializer.signin import SigninSerializer
from mroom.api.serializer.signup import SignupSerializer
from mroom.api.serializer.user import CurrentUserSerializer


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
        data={
            'detail': f'Signup was successful, '
                      f'registration email was sent to {user.email}'
        }
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

    session: Session = Session.objects.create(user=user)

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