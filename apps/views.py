from django.shortcuts import render
from django.http import HttpResponse
from apps.models import *
from apps.forms import *


# Create your views here.

def inicio(request):
    return render(request, "index.html")


#--------------------------------------------------------------------------

def forms_curso(request):
        
    if request.method=="POST":
        
        mi_formulario=Forms_Curso(request.POST)
        
        if mi_formulario.is_valid():
            
            info=mi_formulario.cleaned_data
            
            data_save=Curso(
                nombre=info["nombre"],
                camada=info["camada"],
            )
            
            data_save.save()
            
            return render(request, "apps/save_data.html")
    
    contexto={
        "form": Forms_Curso(),
    }
    
    return render(request, "apps/forms_cursos.html", context=contexto)

def forms_estudiantes(request):

    if request.method=="POST":
        
        mi_formulario=Forms_Estudiantes(request.POST)
        
        if mi_formulario.is_valid():
            
            info=mi_formulario.cleaned_data
            
            data_save=Estudiantes(
                nombre=info["nombre"],
                apellido=info["apellido"],
                email=info["email"]
            )
            
            data_save.save()
            
            return render(request, "apps/save_data.html")

    
    contexto={
        "form": Forms_Estudiantes,
    }
    
    return render(request, "apps/forms_estudiantes.html", context=contexto)

def forms_profesores(request):

    if request.method=="POST":
        
        mi_formulario=Forms_Profesores(request.POST)
        
        if mi_formulario.is_valid():
            
            info=mi_formulario.cleaned_data
            
            data_save=Profesor(
                nombre=info["nombre"],
                apellido=info["apellido"],
                email=info["email"],
                profesion=info["profesion"],
                fecha_nacimiento=info["fecha_nacimiento"],
            )
            
            data_save.save()
            
            return render(request, "apps/save_data.html")

    
    contexto={
        "form": Forms_Profesores,
    }
    
    return render(request, "apps/forms_profesores.html", context=contexto)

def forms_tareas(request):

    if request.method=="POST":
        
        mi_formulario=Forms_Tareas(request.POST)
        
        if mi_formulario.is_valid():
            
            info=mi_formulario.cleaned_data
            
            data_save=Tareas(
                nombre=info["nombre"],
                fecha_entrega=info["fecha_entrega"],
                entregado=info["entregado"]
            )
            
            data_save.save()
            
            return render(request, "apps/save_data.html")

    
    contexto={
        "form": Forms_Tareas,
    }
    
    return render(request, "apps/forms_tareas.html", context=contexto)


#--------------------------------------------------------------------------

def buscar(request):
    
    contexto={
        "forms_curso": Buscar_Forms_Curso(),
        "forms_estudiantes": Buscar_Forms_Estudiantes(),
        "forms_profesores": Buscar_Forms_Profesores(),
        "forms_tareas": Buscar_Forms_Tareas(),
    }    
    
    return render(request, "Apps/buscar.html", context=contexto)



def show_cursos(request):
    
    mi_formulario = Buscar_Forms_Curso(request.GET)
    
    if mi_formulario.is_valid():
        
        info=mi_formulario.cleaned_data
        
        filtrados=Curso.objects.filter(camada__icontains=info["camada"])
        
        contexto={
            "cursos": filtrados,
        }    
    
        
    return render(request, "apps/buscar_cursos.html", context=contexto)


def show_estudiantes(request):
    
    mi_formulario = Buscar_Forms_Estudiantes(request.GET)
    
    if mi_formulario.is_valid():
        
        info=mi_formulario.cleaned_data
        
        filtrados=Estudiantes.objects.filter(email__icontains=info["email"])
        
        contexto={
            "estudiantes": filtrados,
        }    
        
    return render(request, "apps/buscar_estudiantes.html", context=contexto)


def show_profesores(request):
    
    mi_formulario = Buscar_Forms_Profesores(request.GET)
    
    if mi_formulario.is_valid():
        
        info=mi_formulario.cleaned_data
        
        filtrados=Profesor.objects.filter(email__icontains=info["email"])
        
        contexto={
            "profesores": filtrados,
        }    
        
    return render(request, "apps/buscar_profesores.html", context=contexto)


def show_tareas(request):
    
    mi_formulario = Buscar_Forms_Tareas(request.GET)
    
    if mi_formulario.is_valid():
        
        info=mi_formulario.cleaned_data
        
        filtrados=Tareas.objects.filter(nombre__icontains=info["nombre"])
        
        contexto={
            "tareas": filtrados,
        }    
        
    return render(request, "apps/buscar_tareas.html", context=contexto)


