from rest_framework import serializers

class SignupSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    terms = serializers.BooleanField()
    password = serializers.CharField(
        max_length=16,
        min_length=8,
        required=True
    )