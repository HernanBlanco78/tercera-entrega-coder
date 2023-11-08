
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q

from blog_cocina.blogcocina.models import Cocineros, Recetas , Comentarios

# Create your views here.

def listar_recetas(request):
    contexto = {
        "blogcocina":Recetas.objects.all()  
    }
    Http_response= render(
        request = request,
        template_name="blogcocina/recetas.html",
        context=contexto,     
    )
    return Http_response

def listar_Cocineros(request):
    contexto = {
        "blogcocina":Cocineros.objects.all()
    }
    http_response=render(
        request = request,
        template_name="blogcocina/cocineros.html",
        context = contexto,
    )
    return http_response

def agregar_comentarios(request):
    contexto = {
        "blogcocina":Comentarios.objects.all()
    }
    http_response=render(
        request = request,
        template_name="blogcocina/comentarios.html"
        context = contexto,
    )
    return http_response
