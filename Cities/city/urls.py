from django.urls import path
from . import views

app_name="cities"

urlpatterns=[
    path("home/", views.home, name="home_page"),
    path("riyadh/",views.city_R,name="riyadh_page"),
    path("abha/",views.city_A,name="abha_page"),
    path("makkah/",views.city_M,name="makkah_page"),
    path("alula/",views.city_AL,name="alula_page")
]

