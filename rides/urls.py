from django.urls import path
from . import views

urlpatterns = [
    path("vehicles/add/", views.add_vehicle, name="add-vehicle"),
    path("journeys/", views.JourneyListCreateView.as_view(), name="journey-list-create"),
    path("bookings/create/", views.create_booking, name="create-booking"),
    path("bookings/my/", views.my_bookings, name="my-bookings"),
    path("drivers/", views.DriverListCreateView.as_view(), name="driver-list-create"),
]  