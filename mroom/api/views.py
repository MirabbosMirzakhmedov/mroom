from django.http.request import HttpRequest
from django.http.response import JsonResponse
from rest_framework import serializers
from mroom.api.models import User


from rest_framework.decorators import api_view
from mroom.api.serializers import SignupSerializer
import typing
import json

@api_view(['POST'])
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
    terms: bool = serializer.data.get('terms')
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
        terms=terms,
        name=name,
    )

    return JsonResponse(
        status=201,
        data={
            'detail': 'success'
        }
    )
