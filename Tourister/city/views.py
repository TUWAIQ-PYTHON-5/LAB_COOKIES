from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.

# def main_page(request : HttpRequest):

#     return render(request, "city/index.html")

def riyadh_page(request : HttpRequest):

    return render(request, "city/riyadh.html")

def abha_page(request : HttpRequest):

    return render(request, "city/abha.html")

def mekkah_page(request : HttpRequest):

    return render(request, "city/mekkah.html")

def alUla_page(request : HttpRequest):

    return render(request, "city/alUla.html")

