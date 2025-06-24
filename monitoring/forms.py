from django import forms
from .models import CCTV, PoliceStation

class CCTVForm(forms.ModelForm):
    class Meta:
        model = CCTV
        fields = '__all__'

class PoliceStationForm(forms.ModelForm):
    class Meta:
        model = PoliceStation
        fields = '__all__'
