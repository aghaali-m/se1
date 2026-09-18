from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def show_temp_view(request):
    return HttpResponse("همدان 27 درجه سانتی گراد")