from django.urls import path
from . import views

app_name = "city"

urlpatterns = [
    #path("", views.main_page, name="main_page"),
    path("abha/", views.abha_page, name="abha_page"),
    path("alUla/", views.alUla_page, name="alUla_page"),
    path("mekkah/", views.mekkah_page, name="mekkah_page"),
    path("riyadh/", views.riyadh_page, name="riyadh_page"),
    
]