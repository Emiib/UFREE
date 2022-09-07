from email.message import EmailMessage
from django.shortcuts import render
from django.http import HttpResponse
from .models import Jobs, Client, DateProject
from .forms import JobsForm, ClienteForm, DateProjectForm
from django.views import *


def inicio(request,):
    return render (request, "inicio.html")

def Job(request):
    tipo = request.POST.get("tipo")
    id = request.POST.get("id")
    Job = Job(tipo=tipo, id=id)
    Job.save()
    texto="Job Created"
    return HttpResponse(texto)


def jobs_view(request):
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

def clienty(request):
    nombre = request.POST.get("nombre")
    apellido = request.POST.get("apellido")
    email = request.POST.get("email")
    dni = request.POST.get("dni")
    clienty = clienty(nombre=nombre, apellido=apellido, email = email, dni=dni)
    clienty.save()
    texto="Client created"
    return HttpResponse(texto)


def Clients_view(request):
      if request.method == 'POST':
            formulario = ClienteForm(request.POST)
            print(formulario)
            if formulario.is_valid:  
                  info = formulario.cleaned_data
                  nombre = info["nombre"]
                  apellido = info["apellido"]
                  email = info["email"]
                  dni = info["dni"]
                  clienty = Client(nombre = nombre, apellido=apellido,email = email, dni = dni) 
                  clienty.save()
                  return render(request,"inicio.html") 

      else: 
            formulario= ClienteForm()
      
      return render(request, "Client.html", {"formulario":formulario})


def datepr(request):
    first_deliver = request.POST.get("first_deliver")
    second_deliver = request.POST.get("second_deliver")
    delivered = request.POST.get("delivered")
    datepr = datepr(first_deliver=first_deliver, second_deliver=second_deliver, delivered = delivered)
    datepr.save()
    texto="Date Added"
    return HttpResponse(texto)

def DateProjects_view(request):
      if request.method == 'POST':
            formulario = DateProjectForm(request.POST)
            print(formulario)
            if formulario.is_valid:  
                  info = formulario.cleaned_data
                  first_deliver = info["first_deliver"]
                  second_deliver = info["second_deliver"]
                  deliverd = info["deliverd"]
                  datepr = DateProject(first_deliver = first_deliver, second_deliver=second_deliver,deliverd = deliverd) 
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
            jobs = Jobs.objects.filter  (id=id)
            return render(request,"searchresults.html", {'jobs':jobs})

      else:
            mensaje = "please, enter an ID"
            
      return render(request, "searchresults.html", {'mensaje': mensaje})
            

