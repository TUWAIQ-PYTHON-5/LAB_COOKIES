from django.urls import path
from . import views


app_name='cities'

urlpatterns=[
    path('',views.home,name='home page'),
    path('city/Riyadh/',views.riyadh,name='riyadh page'),
    path('city/Abha/',views.abha,name='abha page'),
    path('city/Mekkah/',views.mekkah,name='mekkah page'),
    path('city/AlUla/',views.alula,name='alula page'),
    path('mode/dark/',views.dark_mode,name='mode_dark'),
    path('mode/light/',views.light_mode,name='mode_light'),
]
