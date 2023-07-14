from django.urls import path
from AppCoder import views

urlpatterns = [
    path("", views.inicio, name='Inicio'), #esta era nuestra primer view
    path('verCursos', views.busquedaCamada, name='Ver Cursos'),
    path('cursos', views.cursos, name='Cursos'),
    path('profesores', views.profesor, name='Profesores'),
    path('estudiantes', views.estudiantes, name='Estudiantes'),
    path('entregables', views.entregables, name='Entregables'),
    path('cursoFormulario', views.CursoFormulario, name="CursoFormulario"),
    path('profesorFormulario', views.profesor, name='ProfesorFormulario'),
    path('busquedaCamada', views.busquedaCamada, name="BusquedaCamada"),
    path('buscar', views.buscar),
]
