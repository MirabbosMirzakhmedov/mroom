import json
import typing

import requests
from django.db.transaction import atomic
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view

from mroom import settings
from mroom.api.email.campaign import Signup
from mroom.api.exceptions import ServiceUnavailable, AuthenticationFailed
from mroom.api.models import User
from mroom.api.serializers import SignupSerializer, SigninSerializer


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
def signin(request: HttpRequest) -> JsonResponse:
    signin_data: typing.Dict = json.loads(request.body)

    serializer = SigninSerializer(data=signin_data)
    serializer.is_valid(raise_exception=True)

    email: str = serializer.data.get('email')

    query_set = User.objects.filter(
        email=email)

    if query_set.exists() == False:
        raise AuthenticationFailed()

    # our user
    user = query_set.first()

    if user.check_password(
            raw_password=serializer.data.get(
                'password'
            )
    ) == False:
        raise AuthenticationFailed()





    return JsonResponse(
        status=201,
        data={
            'detail': 'success'
        }
    )
