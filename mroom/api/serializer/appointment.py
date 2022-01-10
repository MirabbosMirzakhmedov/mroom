from rest_framework import serializers
from mroom.api.models import User


class AppointmentSerializer(serializers.ModelSerializer):
    barber = serializers.SlugRelatedField(
        many=False,
        slug_field='uid',
        queryset=User.objects.filter(is_barber=True),
        required=True
    )