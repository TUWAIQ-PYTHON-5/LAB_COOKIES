from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
# Create your views here.

def home(request):
    return render(request,'cities/home.html')

def riyadh(request):
    return render(request,'cities/riyadh.html')

def abha(request):
    return render(request,'cities/abha.html')

def mekkah(request):
    return render(request,'cities/mekkah.html')

def alula(request):
    return render(request,'cities/alula.html')






def dark_mode(request : HttpRequest):
    response = render(request, 'cities/home.html')
    response.set_cookie("mode","dark", max_age=60*60*24*7)
    return response


def light_mode(request : HttpRequest):

    response = render(request, 'cities/home.html')
    response.set_cookie("mode","light", max_age=60*60*24*7)
    return response
