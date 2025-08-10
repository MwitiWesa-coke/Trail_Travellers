from django.db import models
from accounts.models import Driver
from accounts.models import CustomUser

# Vehicle model

class Vehicle(models.Model):
    #Our Vehicles
    VEHICLE_TYPES = (
        ('suv', 'SUV'),
        ('car', 'Car'),
        ('bike', 'Bike'),
        ('van', 'Van'),
        ('bus', 'Bus'),
    )

    # vehicle owner = driver
    owner = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='vehicles')
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPES)
    #Unique Number Plates
    registration_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.vehicle_type} - {self.registration_number}"


#JOURNEY MODEL
class Journey(models.Model):
    #driver being assigned to the journey
    client = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='client_journeys', null=True, blank=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='driver_journeys', null=True, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True, related_name='journeys')
    #start and end of journey
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    #when journey is supposed to start
    departure_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


    def __str__(self):
        driver_name = self.driver.user.full_name if self.driver else "No driver"
        vehicle_info = ( 
            f"{self.vehicle.vehicle_type} - {self.vehicle.registration_number}"
            if self.vehicle else "no vehicle"
        )
        return f"{self.origin} to {self.destination} by {driver_name} ({vehicle_info})"


#Booking Model
class Booking(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='bookings')
    journey = models.ForeignKey(Journey, on_delete=models.CASCADE, related_name='bookings')
    booking_time = models.DateTimeField(auto_now_add=True)

    #confirm booking
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking by {self.client.full_name} for {self.journey}"
