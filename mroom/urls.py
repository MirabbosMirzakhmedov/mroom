import debug_toolbar
from django.conf import settings
from django.urls import path, include
from rest_framework_nested.routers import SimpleRouter
import typing

from mroom.api.views import (
    signup,
    signin,
    signout,
    CurrentUserViewSet,
    BarberViewSet,
    AppointmentViewSet,
)
from mroom.report.views import SurveyViewSet

viewsets: typing.List[typing.Dict] = [
    {
        'prefix': r'api/current_user',
        'viewset': CurrentUserViewSet,
        'basename': 'current_user'
    },
    {
        'prefix': r'api/appointment',
        'viewset': AppointmentViewSet,
        'basename': 'appointment'
    },
    {
        'prefix': r'api/barber',
        'viewset': BarberViewSet,
        'basename': 'barber'
    },
    {
        'prefix': r'api/survey',
        'viewset': SurveyViewSet,
        'basename': 'survey'
    }
]

router = SimpleRouter()

for viewset in viewsets:
    router.register(
        prefix=viewset['prefix'],
        viewset=viewset['viewset'],
        basename=viewset['basename']
    )

urlpatterns = [
    path('api/signup/', signup),
    path('api/signin/', signin),
    path('api/signout/', signout),
]

if settings.DEBUG:
    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls))
    )

urlpatterns = urlpatterns + router.urls
