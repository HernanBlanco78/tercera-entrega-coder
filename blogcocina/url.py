from django.contrib import admin
from django.urls import path, include

from blogcocina.views import ( Recetas, Cocineros, Comentarios)




urlpatterns = [
    
    path("blogcocina/",Recetas),
    path("blogcocina/",Cocineros),
    path("blogcocina/",Comentarios)
]
