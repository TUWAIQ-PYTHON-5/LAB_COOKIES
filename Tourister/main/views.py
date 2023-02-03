from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse

# Create your views here.


def consent_to_TOS(request : HttpRequest):

    response = redirect("main:home_page")
    response.set_cookie("consent", "Yes")

    return response

def set_dark_mode (request : HttpRequest):
    
    response = redirect("main:home_page")
    
    response.set_cookie("mode","dark", max_age=60*60*24*7)
    
    return response


def set_ligth_mode (request : HttpRequest):
    response = redirect("main:home_page")
    response.set_cookie("mode","dight", max_age=60*60*24*7)

    return response

def Home (request : HttpRequest):
    
    return render(request ,"main/home.html")

def Riyadh (request : HttpRequest):

    return render(request ,"main/Riyadh.html")


def Qassim (request : HttpRequest):

    return render(request ,"main/Qassim.html")


def Mekkah (request : HttpRequest):

    return render(request ,"main/Mekkah.html")

def AlUla (request : HttpRequest):


    return render(request ,"main/AlUla.html")