from django.urls import path
from . import views

app_name = "main"

urlpatterns= [
    path('', views.Home, name="home_page"),
    path("city/Riyadh/", views.Riyadh, name="Riyadh_page"),
    path("city/Qassim/", views.Qassim, name="Qassim_page"),
    path("city/Mekkah/", views.Mekkah, name="Mekkah_page"),
    path("city/AlUla/", views.AlUla, name="AlUla_page"),
    path("consent/tos/", views.consent_to_TOS, name="consent_to_tos"),
    path("mode/dark/", views.set_dark_mode, name="mode_dark"),
    path("mode/light/", views.set_ligth_mode, name="mode_light"),



]
