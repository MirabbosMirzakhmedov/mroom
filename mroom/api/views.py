from django.http.request import HttpRequest
from django.http.response import JsonResponse


from rest_framework.decorators import api_view
from mroom.api.serializers import SignupSerializer
import typing
import json

@api_view(['POST'])
def signup(request: HttpRequest) -> JsonResponse:
    signup_data: typing.Dict = json.loads(request.body)

    serializer = SignupSerializer(data=signup_data)
    serializer.is_valid(raise_exception=True)

    return JsonResponse(
        status=201,
        data={
            'detail': 'success'
        }
    )
