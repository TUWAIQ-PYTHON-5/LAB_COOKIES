from django.shortcuts import render , resolve_url , redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.


def home(request : HttpRequest):

    return render(request , "main/home.html" )



def riyadh(request : HttpRequest):
    riyadh_url = resolve_url("main:riyadh")
    return render(request , "main/riyadh.html" )




def almaa(request : HttpRequest):

    return render(request , "main/almaa.html" )




def makah(request : HttpRequest):

    return render(request , "main/makah.html" )



def madinah(request : HttpRequest):

    return render(request , "main/madinah.html" )





def cookes(request : HttpRequest):

    response = redirect("main:home")
    response.set_cookie("consent", "Yes", max_age=60*60*24*30)

    return response


def set_dark_mode(request : HttpRequest):

    response = redirect("main:index_page")
    response.set_cookie("mode", "dark", max_age=60*60*24*7)

    return response


def set_light_mode(request : HttpRequest):

    response = redirect("main:index_page")
    response.set_cookie("mode", "light", max_age=60*60*24*7)

    return response
