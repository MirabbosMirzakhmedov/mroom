from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
import typing
import json


@require_http_methods(['GET'])
def get_sample(r: HttpRequest) -> HttpResponse:

    return HttpResponse(
        status=200,
        content=b'This is not a sample content'
    )

# @api_view(['POST'])
def signup(request: HttpRequest) -> HttpResponse:

    signup_data: typing.Dict = json.loads(request.body)
    print(signup_data)

    return HttpResponse(
        status=201,
        data={
            'detail': 'success'
        }
    )