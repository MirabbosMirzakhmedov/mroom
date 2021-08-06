from django.contrib import admin
from django.urls import path

from mroom.api.views import (
    signup,
    signin,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signup/', signup),
    path('api/signin/', signin),
]
