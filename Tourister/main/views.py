from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.



#first page
def home_page(request : HttpRequest):
    return render(request, "main/home.html")

#second page
def Aola_city(request : HttpRequest):
    return render(request, "main/Alola.html")

#therd page
def Albaha_city(request : HttpRequest):
    return render(request, "main/Albaha.html")

#fourth page
def Makkah_city(request : HttpRequest):
    return render(request, "main/Makkah.html")

#fifth page
def Tabuk_city(request : HttpRequest):
    return render(request, "main/Tabuk.html")


def set_dark_mode(request : HttpRequest):

    response = redirect("main:home_page")
    response.set_cookie("mode", "dark", max_age=60*60*24*7)

    return response


def set_light_mode(request : HttpRequest):

    response = redirect("main:home_page")
    response.set_cookie("mode", "light", max_age=60*60*24*7)

    return response  


