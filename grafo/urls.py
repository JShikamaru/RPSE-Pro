from django.contrib import admin
from django.urls import path
from .views import grafo,getGrafo

app_name = "grafo"

urlpatterns = [
    path('grafo/', grafo, name= "grafo"),
    path('grafo/clasificar', getGrafo, name= "grafoClasifica")
]