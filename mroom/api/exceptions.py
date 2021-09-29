from rest_framework import status
from rest_framework.exceptions import APIException


class ServiceUnavailable(APIException):
    status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    default_detail = 'Service Unavailable'
    default_code = 'service_unavailable'


class AuthenticationFailed(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'Incorrect authentication credentials'
    default_code = 'authentication_failed'


class AuthorizationFailed(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'Authorization cookie missing'
    default_code = 'authorization_failed'


class SessionFailed(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'Invalid session or inactive user'
    default_code = 'session_failed'
