from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from .models import Jobs, Client, DateProject
from .forms import JobsForm, ClienteForm, DateProjectForm
from django.views import *


def Job(request):
    tipo = request.POST.get("tipo")
    id = request.POST.get("id")
    job = Job(nombre=tipo, id=id)
    job.save()
    texto=f"Job Created"
    return HttpResponse(texto)


def inicio(request,):
    return render (request, "inicio.html")

def Jobs(request):
    return render (request, "Jobs.html")

def Client(request):
      return render(request, "Client.html")    

def DateProject(request):
      return render(request, "dateproject.html")

def Jobs(request):
      if request.method == 'POST':
            formulario = JobsForm(request.POST)
            print(formulario)
            if formulario.is_valid:   
                  info = formulario.cleaned_data
                  tipo = info["tipo"]
                  id = info["id"]
                  job = Job(tipo=tipo, id=id)
                  job.save()
                  return render(request,"inicio.html")
      else:
            formulario = JobsForm()

      return render(request, "Jobs.html", {"formulario":formulario})


def Clients(request):
      if request.method == 'POST':
            formulario = ClienteForm(request.POST)
            print(formulario)
            if formulario.is_valid:  
                  info = formulario.cleaned_data
                  client = Client(nombre = info['nombre'], apellido=info['apellido'],email = info['email'], dni = info['dni']) 
                  client.save()
                  return render(request,"inicio.html") 

      else: 

            formulario= ClienteForm()

      return render(request, "Client.html", {"formulario":formulario})




def DateProjects(request):
      if request.method == 'POST':
            FormDatePr = DateProjectForm(request.POST)
            print(FormDatePr)
            if FormDatePr.is_valid:  
                  info = FormDatePr.cleaned_data
                  datepr = DateProject(nombre = info['nombre'], apellido=info['apellido'],email = info['email'], dni = info['dni']) 
                  datepr.save()
                  return render(request,"inicio.html")

      else: 

            FormDatePr= DateProjectForm()

      return render(request, "dateproject.html", {"FormDatePr":FormDatePr})


def search(request):

      if  request.GET["id"]:

            id = request.GET['id'] 
            tipo = Jobs.objects.filter(id__icontains=id)
            return render(request,"inicio.html", {"tipo":tipo, "id":id})

      else:
            answer = "¿Buscas algun dato?"

      return render(request,"search.html", {"respuesta":answer})

