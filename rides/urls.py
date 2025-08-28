from django.urls import path
from . import views

urlpatterns = [
    path("vehicles/add/", views.add_vehicle, name="add-vehicle"),
    path("journeys/", views.list_journeys, name="list-journeys"),
    path("bookings/create/", views.create_booking, name="create-booking"),
    path("bookings/my/", views.my_bookings, name="my-bookings"),
] 