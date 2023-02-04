from django.shortcuts import render,resolve_url,redirect
from django.http import HttpRequest,HttpResponse


# Create your views here.
def set_dark(request:HttpRequest):
    response = render(request, 'main/base.html')
    response.set_cookie('mode','dark')
    return response

def set_light(request:HttpRequest):
    response=render(request,'main/base.html')
    response.set_cookie('mode','light')
    return response

def home_page(request:HttpRequest):
 return render(request,"main/base.html")




def riyadh_page(request:HttpRequest):
    return render(request,"main/riyadh.html")

def abha_page(request:HttpRequest):

    return render(request,"main/abha.html")

def mekkah_page(request:HttpRequest):

    return render(request,"main/makkah.html")

def alula_page(request:HttpRequest):

    return render(request,"main/alula.html")


    
