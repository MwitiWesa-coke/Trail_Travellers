from rest_framework import serializers
from .models import CustomUser, Driver, Admin

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email", "full_name", "phone", "role", "date_joined"]
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        return user

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