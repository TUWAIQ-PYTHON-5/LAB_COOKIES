from django.shortcuts import render,resolve_url,redirect
from django.http import HttpRequest,HttpResponse

# Create your views here.
def home_page(request:HttpRequest):


    return render(request ,'main/base.html'  )


def riyadh_page(request:HttpRequest):

    return render(request ,'main/Riyadh.html' )   


def abha_page(request :HttpRequest):

    return render(request , 'main/Abha.html' )   

def makkah_page(request : HttpRequest):
    
    return render(request,'main/Mekkah.html')  

def Alula(request :HttpRequest):
    return render(request , 'main/AlUla.html')




def set_dark_mode(request : HttpRequest):

    response = redirect("main:home_page")
    response.set_cookie("mode", "dark", max_age=60*60*24*7)

    return response


def set_light_mode(request : HttpRequest):

    response = redirect("main:home_page")
    response.set_cookie("mode", "light", max_age=60*60*24*7)

    return response    