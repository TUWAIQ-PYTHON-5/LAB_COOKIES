from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
{'% load static %'}
def home_page(request : HttpRequest):
    return render(request,"Main/Home_Page.html")

def city_riyadh(request : HttpRequest):
    return render(request,"Main/riyadh.html")

def city_alula(request : HttpRequest):
    return render(request,"Main/alula.html")

def city_mekkah(request : HttpRequest):
    return render(request,"Main/mekkah.html")

def city_abha(request : HttpRequest):
    return render(request,"Main/abha.html")


def light_mode(request : HttpRequest):
    mode = render(request,"Main/home_page.html")
    mode.set_cookie('mode','light',max_age=(60*60*24)*7)
    
    return mode

def dark_mode(request : HttpRequest):
    mode = render(request,"Main/home_page.html")
    mode.set_cookie('mode','dark',max_age=(60*60*24)*7)
    
    return mode