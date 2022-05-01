from rest_framework import serializers

from mroom.api import models


class CurrentUserSerializer(serializers.ModelSerializer):
    survey_uid = serializers.SerializerMethodField()

    class Meta:
        model = models.User
        fields = [
            'uid',
            'name',
            'survey_uid'
        ]

    def get_survey_uid(self, object):
        survey = object.surveys.get(key='default')

        return str(survey.uid)
