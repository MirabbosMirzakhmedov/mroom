from rest_framework import serializers
from mroom.api.models import Appointment


class PhoneNumberField(serializers.RegexField):
    default_error_messages = {
        'invalid': 'Must be without spaces and '
                   'cannot have more less than 9 and more than 15 characters.'
    }

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            'full_name',
            'phone_number',
            'date',
            'barber',
            'message',
        ]

    phone_number = PhoneNumberField(
        regex=r'^\+?1?\d{9,15}$',
    )

