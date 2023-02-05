from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_page , name="home_page"),
    path("city/Riyadh/", views.riyadh_page, name="riyadh_page"),
    path("city/Abha/", views.abha_page, name="abha_page"),
    path("city/Makkah/", views.makkah_page, name="makkah_page"),
    path("city/AlUla/",views.alula_page, name="alula_page"),
    path("mode/dark/", views.set_dark_mode, name="mode_dark"),
    path("mode/light/", views.set_light_mode, name="mode_light"),
]