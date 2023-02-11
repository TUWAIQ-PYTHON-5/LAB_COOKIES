
from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse


def home_page(request : HttpRequest):
   
    return render(request , "main/home.html")



def riyadh_page(request : HttpRequest):
   
    return render(request , "main/riyadh.html")

def abha_page(request : HttpRequest):
   
    return render(request , "main/abha.html")

def makkah_page(request : HttpRequest):
   
    return render(request , "main/makkah.html")

def alula_page(request : HttpRequest):
   
    return render(request , "main/alula.html")

def set_dark_mode(request : HttpRequest):

    response = redirect("main:home_page")
    response.set_cookie("mode", "dark", max_age=60*60*24*7)

    return response

def set_light_mode(request : HttpRequest):

    response = redirect("main:home_page")
    response.set_cookie("mode", "light", max_age=60*60*24*7)

    return response  