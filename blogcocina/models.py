from django.db import models

# Create your models here.
class Recetas(models.Model):
    
    nombre = models.CharField(max_length=256)
    ingrediente_principal = models.CharField(max_length=256)
    ingrediente_2= models.CharField(max_length=256)
    tiempo_coccion= models.IntegerField()
    
    
class Cocineros(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    
class Comentarios(models.Model):
    comentario= models.CharField(max_length=300)
    
    