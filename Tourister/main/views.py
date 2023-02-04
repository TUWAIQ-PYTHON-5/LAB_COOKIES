from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse

def base_page(request : HttpRequest):
   
    return render(request , "main/base.html")



def riyadh_page(request : HttpRequest):
   
    return render(request , "main/riyadh.html")

def abha_page(request : HttpRequest):
   
    return render(request , "main/abha.html")

def mekkah_page(request : HttpRequest):
   
    return render(request , "main/mekkah.html")

def alula_page(request : HttpRequest):
   
    return render(request , "main/alula.html")




def set_dark_mode(request : HttpRequest):

    response = redirect("main:base_page")
    response.set_cookie("mode", "dark", max_age=60*60*24*7)

    return response


def set_light_mode(request : HttpRequest):

    response = redirect("main:base_page")
    response.set_cookie("mode", "light", max_age=60*60*24*7)

    return response  