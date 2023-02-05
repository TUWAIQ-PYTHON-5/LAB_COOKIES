from django.shortcuts import render, resolve_url, redirect
from django.http import HttpRequest, HttpResponse
from datetime import date

# Create your views here.

def index(request : HttpRequest):
    title:      str= "Tourister"
    phrase:     str= "روح السعودية"
    paragraph:  str= "Saudi Arabia’s rich heritage and traditions have been shaped by its position as a historic trade hub and the birthplace of Islam. In recent years, the Kingdom has undergone a significant cultural transformation, evolving centuy-old customs to fit the contemporary world we live in today. Design your tour in the Kingdom of Saudi Arabia by chosing city that you wish to visit. Spring in Saudi Arabia can be brisk, particularly in the north, where the temperature at night can drop below 15 degrees C. The central and southern regions are warmer, averaging around 20 degrees after nightfall. Rainfall is at its highest during spring, particularly in the central region and in the southwest over the Aseer Mountains. Don’t forget to pack layers — like light sweaters, scarves or pashminas — plus a rain jacket and sunglasses."
    citiesList: list= ['Riyadh', 'Jeddah', 'Taif', 'Ula']
    context = {
        "title" : title,
        "phrase" : phrase,
        "paragraph" : paragraph,
        "citiesList" : citiesList,
    }
    return render(request , "main/index.html", context)

def riyadh (request : HttpRequest):
    title:      str= "Tourister"
    phrase:     str= "فوق الخيال"
    citiesList: list= ['Riyadh', 'Jeddah', 'Taif', 'Ula']
    context = {
        "title" : title,
        "phrase" : phrase,
        "citiesList" : citiesList,
    }
    today = date.today()
    response=render(request , "main/Riyadh.html", context)
    response.set_cookie("visiting_date",today)
    return response

def jeddah (request : HttpRequest):
    title:      str= "Tourister"
    phrase:     str= "أيامنا الحلوة"
    citiesList: list= ['Riyadh', 'Jeddah', 'Taif', 'Ula']
    context = {
        "title" : title,
        "phrase" : phrase,
        "citiesList" : citiesList,
    }
    today = date.today()
    response=render(request , "main/Jeddah.html", context)
    response.set_cookie("visiting_date",today)
    return response
    

def taif (request : HttpRequest):
    title:      str= "Tourister"
    phrase:     str= "مدينة الورود"
    citiesList: list= ['Riyadh', 'Jeddah', 'Taif', 'Ula']
    context = {
        "title" : title,
        "phrase" : phrase,
        "citiesList" : citiesList,
    }
    today = date.today()
    response=render(request , "main/Taif.html", context)
    response.set_cookie("visiting_date",today)
    return response
    

def ula (request : HttpRequest):
    title:      str= "Tourister"
    phrase:     str= "لحظات العلا"
    citiesList: list= ['Riyadh', 'Jeddah', 'Taif', 'Ula']
    context = {
        "title" : title,
        "phrase" : phrase,
        "citiesList" : citiesList,
    }
    today = date.today()
    response=render(request , "main/Ula.html", context)
    response.set_cookie("visiting_date",today)
    return response


def consent_toTOS(request :HttpRequest):
    response = redirect("main:index_page")
    response.set_cookie("consent", "Yes", max_age=60*60*24*7)

    return response

def set_dark_mode(request : HttpRequest):

    response = redirect("main:home_page")
    response.set_cookie("mode", "dark", max_age=60*60*24*7)

    return response


def set_light_mode(request : HttpRequest):

    response = redirect("main:home_page")
    response.set_cookie("mode", "light", max_age=60*60*24*7)

    return response 