from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_bage, name="home_bage"),
    path("arar/", views.arar_city, name="arar_city"),
    path("abha/", views.abha_city, name="abha_city"),
    path("riyadh/", views.riyadh_city, name="riyadh_city"),
    path("alula/", views.alula_city, name="alula_city"),
    path("mode/dark/", views.dark_mode,name="darkmode"),
    path("mode/light/", views.light_mode,name="lightmode"),
]