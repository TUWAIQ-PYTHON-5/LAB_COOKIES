from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.

def home(request : HttpRequest):
    response = render(request,"city/home.html")
    response.set_cookie("key", "value", max_age=60*60*24)
    return response

def city_R(request : HttpRequest):
    return render(request,"city/riyadh.html")

def city_A(request : HttpRequest):
    return render(request,"city/abha.html")

def city_M(request : HttpRequest):
    return render(request,"city/makkah.html")

def city_AL(request : HttpRequest):
    return render(request,"city/alula.html")
