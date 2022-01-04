from datetime import datetime

from rest_framework import serializers

from mroom.api.models import Appointment


class PhoneNumberField(serializers.RegexField):
    default_error_messages = {
        'invalid': 'Phone number must be between '
                   '9 - 15 digits and cannot have blank spaces.'
    }


class DateField(serializers.Field):

    def to_representation(self, value):
        return value

    def to_internal_value(self, date):
        time_now = datetime.now()

        if not date:
            raise serializers.ValidationError(
                'This field may not be blank.'
            )

        datetime_object = datetime.strptime(date, '%Y-%m-%dT%H:%M')

        if time_now > datetime_object:
            raise serializers.ValidationError(
                'Cannot insert date in the past.'
            )

        return date


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

    date = DateField()
    phone_number = PhoneNumberField(
        regex=r'^\+?1?\d{9,15}$',
    )
