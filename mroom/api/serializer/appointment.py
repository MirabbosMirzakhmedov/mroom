from rest_framework import serializers

from mroom.api.models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            'full_name',
            'phone_number',
            'date',
            'barber',
            'message'
        ]
