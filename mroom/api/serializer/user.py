import uuid

from rest_framework import serializers

from mroom.api import models as am
from mroom.report import models as rm


class CurrentUserSerializer(serializers.ModelSerializer):
    survey_uid = serializers.SerializerMethodField()

    class Meta:
        model = am.User
        fields = [
            'uid',
            'name',
            'survey_uid'
        ]

    def get_survey_uid(self, user: am.User) -> uuid.UUID:
        return user.surveys.get(key=rm.Survey.DEFAULT).uid
