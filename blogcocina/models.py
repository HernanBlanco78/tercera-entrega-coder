from django.db import models

# Create your models here.
class Recetas(models.Model):
    nombre = models.CharField(max_length=256)
    ingrediente_principal = models.CharField(max_length=256)
    ingrediente_2= models.CharField(max_length=256)
    tiempo_coccion= models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} ({self.ingrediente_principal})"
    
class Cocineros(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return f"{self.apellido} ({self.nombre})"
    
class Comentarios(models.Model):
    comentario= models.CharField(max_length=300)
    
    def __str__(self):
        return f"{self.comentario}"
    