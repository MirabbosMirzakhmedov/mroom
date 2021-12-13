from rest_framework import serializers
from mroom.api.models import Appointment


class PhoneNumberField(serializers.RegexField):
    default_error_messages = {
        'invalid': 'Phone number must be between '
                   '9 - 15 digits and cannot have blank spaces.'
    }

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            'name',
            'phone_number',
            'date',
            'barber',
            'message',
        ]

    phone_number = PhoneNumberField(
        regex=r'^\+?1?\d{9,15}$',
    )

