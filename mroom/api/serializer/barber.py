from rest_framework import serializers
from mroom.api import models

class BarberSerializer(serializers.Serializer):
    class Meta:
        model = models.User
        fields = ['uid', 'full_name']