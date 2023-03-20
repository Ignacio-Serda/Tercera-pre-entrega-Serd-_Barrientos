from django import forms

class Forms_Curso(forms.Form):
    
    nombre=forms.CharField(max_length=40)
    camada=forms.IntegerField()
    
class Forms_Estudiantes(forms.Form):
    
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    email=forms.EmailField()
    
class Forms_Profesores(forms.Form):
    
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    email=forms.EmailField()
    profesion=forms.CharField(max_length=40)
    fecha_nacimiento=forms.DateField()
    
class Forms_Tareas(forms.Form):
    
    nombre=forms.CharField(max_length=40)
    fecha_entrega=forms.DateField()
    entregado=forms.BooleanField(required=False)
    
    
#-----------------------------------------------------------

class Buscar_Forms_Curso(forms.Form):
    
    camada=forms.IntegerField()
    
class Buscar_Forms_Estudiantes(forms.Form):
    
    email=forms.CharField()
    
class Buscar_Forms_Profesores(forms.Form):
    
    email=forms.CharField()
    
class Buscar_Forms_Tareas(forms.Form):
    
    nombre=forms.CharField(max_length=40)