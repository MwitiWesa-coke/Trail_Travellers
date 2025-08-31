from rest_framework import serializers
from .models import Vehicle, Journey, Booking
from accounts.serializers import UserSerializer, DriverSerializer
from accounts.models import Driver

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"

class VehicleSerializer(serializers.ModelSerializer):
    owner = DriverSerializer(read_only=True)

    class Meta:
        model = Vehiclefields = ["id", "owner", "vehicle_type", "registration_number"]


class JourneySerializer(serializers.ModelSerializer):
    client = UserSerializer(read_only=True)
    driver = DriverSerializer(read_only=True)
    vehicle = VehicleSerializer(read_only=True)

    class Meta:
        model = Journey
        fields = [
            "id", "client", "driver", "vehicle", "origin", "destination", "departure_time", "price"
        ]

class BookingSerializer(serializers.ModelSerializer):
    client = UserSerializer(read_only=True)
    journey = JourneySerializer(read_only=True)

    class Meta:
        model = Booking
        fields = [ "id", "client", "journey", "booking_time", "confirmed"]