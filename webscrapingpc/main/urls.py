from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("resultados",views.resultados,name="resultados"),
    path("aboutus",views.nosotros,name="aboutus")
]
