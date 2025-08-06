from django.contrib import admin
from .models import Vehicle, Journey, Booking

#Vehicle admin
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_type', 'registration_number', 'owner')
    search_fields = ('registration_number', 'owner__full_name')

#Journey admin
@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):
    list_display = ('origin', 'destination', 'driver', 'vehicle', 'price', 'depature_time')
    list_filter = ('origin', 'destination', 'depature_time')
    search_fields = ('origin', 'destination', 'driver__full_name')

#Booking Admin
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('client', 'journey', 'booking_time', 'confirmed')
    list_filter = ('confirmed',)
    search_fields = ('client__full_name', 'journet__origin', 'journey__destination')
