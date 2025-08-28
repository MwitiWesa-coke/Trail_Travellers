from rest_framework import serializers
from .models import CustomUser, Driver, Admin

class UserSerializer(serializers.ModelSerializer):
    class Mets:
        model = CustomUser
        fields = [ 
            "id", "email", "full_name", "phone", "role", "date_joined"
        ]

class DriverSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Driver
        fields = [
            "id", "user", "license_numer", "national_id",
            "vehicle_type", "rating", "is_available", "experience_years"
        ]


class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Admin
        fields = ["id", "user"]