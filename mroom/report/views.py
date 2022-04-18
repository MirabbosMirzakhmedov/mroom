from rest_framework import viewsets

from mroom.report import models
from mroom.report.serializers import SurveySerializer
from mroom.api.authentication.api import PrivateAPIAuthentication
from mroom.report.models import Survey


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    authentication_classes = [PrivateAPIAuthentication]
    lookup_field = 'uid'


