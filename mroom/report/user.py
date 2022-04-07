from rest_framework import serializers
from mroom.api import models


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['uid', 'name']
