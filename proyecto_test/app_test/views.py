from django.http import HttpResponse
from django.shortcuts import render
from app_test.models import Curso
from app_test.models import Alumno
from django.template import loader
import datetime


def inicio(request):
    
    return render( request , "index.html" )


def curso(request):
    cursos = Curso.objects.all()
    dicc = { "cursos": cursos}
    plantilla = loader.get_template("plantillas.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)
  


def alta_curso(request , nombre):
    curso = Curso(nombre=nombre , camada=2323)
    curso.save()
    texto = f"Curso: {curso.nombre} Code: {curso.camada}"
    return HttpResponse(texto)

def alta_alumno(request , nombre):
    alumnos = Alumno(nombre=nombre , fecha=datetime.datetime.now())
    alumnos.save()
    texto = f"Curso: {alumnos.nombre} Code: {alumnos.fecha}"
    return HttpResponse(texto)
