from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.\

def index(request : HttpRequest):


    return render(request, "main/index.html" )


def Riyadh_page(request : HttpRequest):


    return render(request, "main/Riyadh.html" )



def Abha_page(request : HttpRequest):


    return render(request, "main/Abha.html" )




def Makkah_page(request : HttpRequest):


    return render(request , "main/Mekkah.html")


def Alula_page(request : HttpRequest):


    return render(request , "main/Ola.html")


def dark_mode(request : HttpRequest):

    response = redirect("city:home_page")
    response.set_cookie("mode", "dark",max_age=60*60*24*7)

    return response

def light_mode(request : HttpRequest):

    response = redirect("city:home_page")
    response.set_cookie("mode", "light",max_age=60*60*24*7)

    return response