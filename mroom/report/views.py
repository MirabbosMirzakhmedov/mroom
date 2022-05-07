from rest_framework import viewsets

from mroom.api.authentication.api import PrivateAPIAuthentication
from mroom.report.models import Survey
from mroom.report.serializers import SurveySerializer


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    authentication_classes = [PrivateAPIAuthentication]
    lookup_field = 'uid'
