from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Driver
from .models import Vehicle, Journey, Booking
from .serializers import VehicleSerializer, JourneySerializer, BookingSerializer

# -- Vehicles - Only driver and Admin can add
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_vehicle(request):
    user = request.user
    if user.role not in ['driver', 'admin']:
        return Response({"error": "Not authorized - Who are you again?"}, status=status.HTTP_403_FORBIDDEN)

    serializer = VehicleSerializer(data=request.data)
    if serializer.is_valid():
        #assign driver based on role
        if user.role == 'driver':
            driver = user.driver_profile
        else:
            driver_id = request.data.get("driver_id")
            try:
                driver = Driver.objects,get(id=driver_id)
            except Driver.DoesNotExist:
                return Response({"error": "Driver not found"}, status=status.HTTP_404_NOT_FOUND)
                
        serializer.save(owner=driver)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --- Journey list 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_journeys(request):
    journeys = Journey.objects.all()
    serializer = JourneySerializer(journeys, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# -- Bookings - only clients and admins can creata

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_booking(request):
    user = request.user
    if user.role not in ['client', 'admin']:
        return Response({"error": "Only clients or admins can book journeys"}, status=status.HTTP_403_FORBIDDEN)

    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(client=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#-- Clients can see only their bookings

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_bookings(request):
    bookings = Booking.objects.filter(client=request.user)
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

