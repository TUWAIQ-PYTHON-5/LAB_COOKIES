from django.urls import path
from . import views
app_name="main"

urlpatterns = [
    path('home/', views.home_page, name='home_page'),
    path('city/Riyadh/',views.riyadh_page, name='riyadh_page'),
    path('city/Abha/', views.abha_page, name='abha_page'),
    path('city/Mekkah/',views.mekkah_page,name='mekkah_page'),
    path('city/AlUla/',views.alula_page,name='alula_page'),
    path('dark/',views.set_dark,name='set_dark'),
    path('light/',views.set_light,name='set_light'),
    

]
