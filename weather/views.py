import random

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def show_temp_view(request):
    temp=random.randint(10,35)
    context={'city':'همدان','temp':temp}
    return render(request,'show_temp.html',context)
