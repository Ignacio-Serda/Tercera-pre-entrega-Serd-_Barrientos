from django.urls import path
from apps.views import *

urlpatterns = [
    path('', inicio,  name="INICIO"),
    path('forms_cursos', forms_curso, name="FORMS_CURSOS"),
    path('forms_estudiantes', forms_estudiantes, name="FORMS_ESTUDIANTES"),
    path('forms_profesores', forms_profesores, name="FORMS_PROFESORES"),
    path('forms_tareas', forms_tareas, name="FORMS_TAREAS"),
    path('buscar', buscar, name="BUSCAR"),
    path('buscar_cursos', show_cursos, name="BUSCAR_CURSOS"),
    path('buscar_estudiantes', show_estudiantes, name="BUSCAR_ESTUDIANTES"),
    path('buscar_profesores', show_profesores, name="BUSCAR_PROFESORES"),
    path('buscar_tareas', show_tareas, name="BUSCAR_TAREAS"),

]
