from django.urls import path
from . import views

app_name = "Main"

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path("city/riyadh/",views.city_riyadh, name='city_riyadh'),
    path("city/alula/",views.city_alula, name='city_alula'),
    path("city/mekkah/",views.city_mekkah, name='city_mekkah'),
    path("city/abha/",views.city_abha, name='city_abha'),
    path('light/mode',views.light_mode, name='light_mode'),
    path('dark/mode',views.dark_mode, name='dark_mode'),
    
]
