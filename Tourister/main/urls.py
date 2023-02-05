from django.urls import path
from. import views

app_name = "main"

urlpatterns =[
    path("",views.home,name="home"),
    path("city/riyadh",views.riyadh,name="riyadh"),
    path("city/almaa",views.almaa,name="almaa"),
    path("city/madenah",views.madinah,name="madinah"),
    path("city/makah",views.makah,name="makah"),
    path("consent/tos/", views.cookes, name="cookes"),
    path("mode/dark/", views.set_dark_mode, name="mode_dark"),
    path("mode/light/", views.set_light_mode, name="mode_light"),
]