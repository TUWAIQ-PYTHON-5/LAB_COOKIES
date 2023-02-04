from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

    
    path("", views.base_page, name="base_page"),
    path("city/Riyadh/", views.riyadh_page, name="riyadh_page"),
    path("city/Abha/", views.abha_page, name="abha_page"),
    path("city/Mekkah/", views.mekkah_page, name="mekkah_page"),
    path("city/Alula/", views.alula_page, name="alula_page"),
    path("mode/dark/", views.set_dark_mode, name="mode_dark"),
    path("mode/light/", views.set_light_mode, name="mode_light"),


]