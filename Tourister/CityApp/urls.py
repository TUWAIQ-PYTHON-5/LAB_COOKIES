from django.urls import path
from . import views

app_name = "city"

urlpatterns = [

    path("", views.index, name="home_page"),
    path("city/Riyadh/", views.Riyadh_page, name="Riyadh_page"),
    path("city/Abha/", views.Abha_page, name="Abha_page"),
    path("city/Mekkah/", views.Makkah_page, name="Makkah_page"),
    path("city/Alula/", views.Alula_page, name="AlUla_page"),
    path("mode/dark/", views.dark_mode, name="dark_mode"),
    path("mode/light/", views.light_mode, name="light_mode")

]