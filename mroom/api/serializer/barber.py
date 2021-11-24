from rest_framework import serializers
from mroom.api import models

class BarberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['uid', 'name']