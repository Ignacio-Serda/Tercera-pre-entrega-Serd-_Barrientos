from django.db import models

# Create your models here.

class Curso(models.Model):
    
    nombre=models.CharField(max_length=40)
    camada=models.IntegerField(unique=True)
    
    def __str__(self):
        return f"Nombre: {self.nombre} Camada: {self.camada}"

class Estudiantes(models.Model):
    
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField(unique=True)
    
    def __str__(self):
        return f"Nombre: {self.nombre} Apellido: {self.apellido} Email: {self.email}"
    
class Profesor(models.Model):
    
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField(unique=True)
    profesion=models.CharField(max_length=40)
    fecha_nacimiento=models.DateField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} Apellido: {self.apellido} Email: {self.email} Profesión: {self.profesion} Fecha_Nacimiento: {self.fecha_nacimiento} "
    
class Tareas(models.Model):
    
    nombre=models.CharField(max_length=40)
    fecha_entrega=models.DateField()
    entregado=models.BooleanField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} Fecha_Entrega: {self.fecha_entrega} Entregado: {self.entregado}"