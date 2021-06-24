from rest_framework.exceptions import APIException

class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service Unavailable'
    default_code = 'service_unavailable'