from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('home/',views.home, name="home"),
    path('Abha/',views.abha, name="city/Abha"),
    path('Mekkah/',views.mekkah, name="city/Mekkah"),
    path('Riyadh/',views.riyadh, name="city/Riyadh"),
    path('AlUla/',views.alula, name="city/AlUla"),
    path("mode/dark/", views.light_mode, name="mode_dark"),
    path("mode/light/", views.dark_mode, name="mode_light"),
]

