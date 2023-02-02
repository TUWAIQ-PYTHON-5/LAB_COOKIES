from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("about/", views.about, name="about_page"),
    path("contact/", views.contact, name="contact_page"),
    path("city/Riyadh/", views.riyadh_page, name="riyadh_page"),
    path("city/Abha/", views.abha_page, name="abha_page"),
    path("city/Mekkah/", views.mekkah_page, name="mekkah_page"),
    path("city/AlUla/", views.alula_page, name="alula_page"),
    path("light/", views.light, name="light_mode"),
    path("dark/", views.dark, name="dark_mode"),
]