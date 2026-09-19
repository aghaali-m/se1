import random

from django.contrib.sites import requests
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def show_temp_view(request):
    lat,lon=37.7981,48.5140
    url=f"https://api.openـmeteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    try:
        data=requests.get(url).json()
        temp=data['current weather']['tempreture']
    except:
        temp=None

    context={'city':'همدان','temp':temp}
    return render(request,'show_temp.html',context)
