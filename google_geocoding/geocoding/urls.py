from django.urls import path
from . import views

urlpatterns = [
    path('geocoding/', views.geocode_form, name='geocoding'),
    path('reverse_geocoding/', views.reverse_geocode_form, name='reverse_geocoding'),
    path('calculate_distance/', views.calculate_distance_form, name='calculate_distance'),
    path('geocoding/result', views.geocode_result, name='geocode_result'),
]