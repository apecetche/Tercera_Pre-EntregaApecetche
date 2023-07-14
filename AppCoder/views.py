from .forms import CursoFormulario
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import *
from AppCoder.forms import *


# Create your views here.
def curso(self):
    curso = Curso(nombre='NombreDeCurso', camada='091218')
    curso.save()

    documentodeTexto = f'--->Curso: {curso.nombre} Camada: {curso.camada}'
    return HttpResponse(documentodeTexto)


def inicio(request):
    return render(request, 'AppCoder/inicio.html')

#def curso(request):
    #return render(request, 'AppCoder/cursos.html')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')


def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')


def entregables(request):
    return render(request, 'AppCoder/entregables.html')


def cursos(request):

    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            curso = Curso(nombre=informacion['nombre'], camada=informacion['camada'])
            curso.save()
            
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = CursoFormulario()

    return render(request, "AppCoder/cursos.html", {"miFormulario": miFormulario})

def profesor(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], 
                                apellido=informacion['apellido'],
                                email=informacion['email'],
                                profesion=informacion['profesion'])
            profesor.save()
            
            return render(request,"AppCoder/inicio.html")
    else:
        miFormulario=ProfesorFormulario()
    
    return render(request, "AppCoder/profesores.html", {"miFormulario":miFormulario})            

def busquedaCamada(request):
    return render(request, "AppCoder/busquedaCamada.html")


def buscar(request):
    if request.method == 'GET':
        # camada = request.GET.get("camada")
        # curso = Curso.objects.filter(camada__icontains=camada)
        # curso = request.GET.get("curso")
        curso = Curso.objects.all()
        return render(request, 'AppCoder/resultadosBusqueda.html', {"curso": curso})
    else:
        # respuesta = 'No enviaste datos.'
        print("asd")
        return render(request, 'AppCoder/resultadosBusqueda.html')
    
    # return HttpResponse(respuesta)