from django.contrib import admin
from django.urls import path

from mroom.api.views import signup
from mroom.views import (
    get_sample
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sample/', get_sample, name='get_sample'),
    path('api/signup/', signup)
]
