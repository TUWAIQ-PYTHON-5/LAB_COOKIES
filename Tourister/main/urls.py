from django.urls import path
from . import views

app_name='main'

urlpatterns = [
    path('' , views.home_page , name='home_page'),
    path('city/Riyadh/' , views.riyadh_page , name='Riyadh_page'),
    path('city/abha/' , views.abha_page , name='Abha_page'),
    path('city/Mekkah/' , views.makkah_page , name='Mekkah_page'),
    path('city/AlUla/' , views.Alula , name='AlUla_page'),
    path("mode/dark/", views.set_dark_mode, name="mode_dark"),
    path("mode/light/", views.set_light_mode, name="mode_light"),
]