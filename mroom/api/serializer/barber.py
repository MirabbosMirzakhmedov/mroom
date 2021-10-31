from rest_framework import serializers

from mroom.api.models import User


class BarberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'name', # <- Here was full_name, and the test didn't work
            'uid',
        ]
