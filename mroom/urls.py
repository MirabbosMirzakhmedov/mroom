from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from django.conf import settings

from mroom.api.views import (
    signup,
    signin,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signup/', signup),
    path('api/signin/', signin),
]

if settings.DEBUG:
    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls))
    )
   