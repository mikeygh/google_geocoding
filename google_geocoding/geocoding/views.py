from django.shortcuts import render
import requests
from google_geocoding.settings import API_KEY
from django.http import HttpResponse
from urllib.parse import urlencode
import json
from django.http import Http404
from .forms import GeocodeForm, ReverseGeocodeForm, CalculateDistanceForm
from geopy.distance import geodesic

def geocode_form(request):
    return return_form(GeocodeForm,request)

def reverse_geocode_form(request):
    return return_form(ReverseGeocodeForm, request)

def calculate_distance_form(request):
    return return_form(CalculateDistanceForm, request)

def return_form(return_form,request):

    if request.method == 'GET':
        form = return_form(request.GET)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = return_form()
    return render(request, 'geocode_form.html', {'form': form})

def geocode_result(request):

    if 'address' in request.GET:
        input = urlencode({'address': request.GET['address']})
        results = get_geocode(input)
        message = json.dumps(results)

    if ['longitude', 'latitude'] == list(request.GET):
        latitude = request.GET['latitude']
        longitude = request.GET['longitude']
        input = urlencode({'latlng': '{},{}'.format(latitude,longitude)})
        results = get_geocode(input)
        message = json.dumps(results)

    if ['latitude_1', 'longitude_1', 'latitude_2', 'longitude_2'] == list(request.GET):
        latitude_1 = request.GET['latitude_1']
        longitude_1 = request.GET['longitude_1']
        latitude_2 = request.GET['latitude_2']
        longitude_2 = request.GET['longitude_2']
        message = get_distance(latitude_1, longitude_1, latitude_2, longitude_2)

    return HttpResponse(message)

def get_geocode(url_string):

    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?{}&key={}'.format(url_string, API_KEY))
    try :
        return response.json().get('results')[0]
    except IndexError:
        print("Error with getting geocode")
        raise Http404


def get_distance(lat_1, lng_1, lat_2, lng_2):

    location_1 = (lat_1,lng_1)
    location_2 = (lat_2, lng_2)
    return "Location 1 and Location 2 are {} miles away from each other".format(geodesic(location_1, location_2).miles)