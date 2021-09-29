import typing

from django.http.request import HttpRequest
from django.utils import timezone
from rest_framework import authentication

from mroom import settings
from mroom.api import models
from mroom.api.exceptions import (
    AuthorizationFailed,
    SessionFailed,
)
from mroom.api.models import Session


class NoAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        return None, None

    def authenticate_header(self, request):
        return 'Cookie'


class PrivateAPIAuthentication(NoAuthentication):

    def authenticate(
            self,
            request: HttpRequest
    ) -> typing.Tuple[models.User, models.Session]:
        session: models.Session = get_authorized_session(
            request=request
        )

        return session.user, session


def get_authorized_session(request: HttpRequest) -> Session:
    token: typing.Union[str, None] = request.COOKIES.get(
        settings.SESSION_COOKIE_NAME)

    if not token:
        raise AuthorizationFailed()

    try:
        return (
            models
                .Session
                .objects
                .select_related('user')
                .get(
                last_active__gte=timezone.now() - settings.SESSION_DURATION,
                token=token,
                is_active=True,
            )
        )

    except Session.DoesNotExist:
        raise SessionFailed()
