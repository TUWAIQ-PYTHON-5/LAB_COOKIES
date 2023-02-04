from django.shortcuts import render,resolve_url, redirect
from django. http import HttpRequest, HttpResponse
# Create your views here.


def home (request: HttpRequest):


    
    return render (request, "main/home.html" )


def abha (request: HttpRequest):


    
    return render (request, "main/Abha.html" )



def alula (request: HttpRequest):


    
    return render (request, "main/AlUla.html" )


def mekkah (request: HttpRequest):


    
    return render (request, "main/Mekkah.html" )

    

def riyadh (request: HttpRequest):


    
    return render (request, "main/Riyadh.html" )



def light_mode(request: HttpRequest):

    response = redirect("main:home")
    response.set_cookie("mode","light",max_age=60*60*24*7)
    
    return response


def dark_mode(request: HttpRequest):

    response = redirect("main:home")
    response.set_cookie("mode","dark",max_age=60*60*24*7)
    
    return response



