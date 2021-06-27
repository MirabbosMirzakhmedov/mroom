from django.http.request import HttpRequest
from django.http.response import JsonResponse
from rest_framework import serializers
from mroom.api.models import User, UserManager
from mroom import settings
from mroom.api.email.campaign import Signup
from mroom.api.exceptions import ServiceUnavailable
from django.db.transaction import atomic

from rest_framework.decorators import api_view
from mroom.api.serializers import SignupSerializer
import typing
import json
import requests


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
                "terms": [
                    "You must accept terms and conditions."
                ]
            }
        )

    email: str = serializer.data.get('email')
    password: str = serializer.data.get('password')
    name: str = serializer.data.get('name')

    exists: bool = User.objects.filter(
        email=email,
    ).exists()

    if exists:
        raise serializers.ValidationError(
            {
                "email": [
                    "This email address is already being used."
                ]
            }
        )

    user: User = User.objects.create_user(
        email=email,
        password=password,
        name=name,
        terms=terms
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
