from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="home_page"),
    path("Riyadh/", views.riyadh, name="Riyadh"),
    path("Jeddah/", views.jeddah, name="Jeddah"),
    path("Taif/", views.taif, name="Taif"),
    path("Ula/", views.ula, name="Ula"),
    path("dark/", views.set_dark_mode, name="mode_dark"),
    path("light/", views.set_light_mode, name="mode_light"),
]