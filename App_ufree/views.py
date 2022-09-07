from django.shortcuts import render
from django.http import HttpResponse
from .models import Jobs, Client, DateProject
from App_ufree.forms import JobsForm, ClienteForm, DateProjectForm
from django.views import *


def Job(request):
    tipo = request.POST.get("tipo")
    id = request.POST.get("id")
    Job = Job(tipo=tipo, id=id)
    Job.save()
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
                  Job = Jobs(tipo=tipo, id=id)
                  Job.save()
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
            formulario = DateProjectForm(request.POST)
            print(formulario)
            if formulario.is_valid:  
                  info = formulario.cleaned_data
                  datepr = DateProject(first_deliver = info['first_deliver'], second_deliver=info['second_deliver'],deliverd = info['delivered']) 
                  datepr.save()
                  return render(request,"inicio.html")
      else: 
            formulario= DateProjectForm()
      return render(request, "dateproject.html", {"formulario":formulario})


def search_id(request):
      return render(request, 'searchresults.html')

def search(request):

      if  request.GET["id"]:

            id = request.GET['id'] 
            Jobs = Jobs.objects.filter(id=id)
            return render(request,"searchresults.html", {'Jobs':Jobs})

      else:
            answer = "¿Buscas algun dato?"

      return render(request,"search.html", {"respuesta":answer})

