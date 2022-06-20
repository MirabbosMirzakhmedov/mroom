from rest_framework import viewsets

from mroom.api.authentication.api import PrivateAPIAuthentication
from mroom.report.models import Survey, Report
from mroom.report.serializers import SurveySerializer, ReportSerializer


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    authentication_classes = [PrivateAPIAuthentication]
    lookup_field = 'uid'


class ReportsViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
