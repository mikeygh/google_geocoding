from django import forms

class GeocodeForm(forms.Form):
    address = forms.CharField(max_length=254)

class ReverseGeocodeForm(forms.Form):
    longitude = forms.CharField(max_length=254)
    latitude = forms.CharField(max_length=254)

class CalculateDistanceForm(forms.Form):
    latitude_1 = forms.CharField(max_length=254)
    longitude_1 = forms.CharField(max_length=254)

    latitude_2 = forms.CharField(max_length=254)
    longitude_2 = forms.CharField(max_length=254)