from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

    path("", views.home_page, name="home_page"),
    path("city/Alola/", views.Aola_city, name="Alola_page"),
    path("city/Albaha/", views.Albaha_city, name="Abaha_page"),
    path("city/Makkah/", views.Makkah_city, name="Makkah_page"),
    path("city/Tabuk/", views.Tabuk_city, name="Tabuk_page"),
    path("mode/dark/", views.set_dark_mode, name="mode_dark"),
    path("mode/light/", views.set_light_mode, name="mode_light")

]