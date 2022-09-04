from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from App_ufree.models import Jobs, Client, DateProject
from App_ufree.forms import JobsForm, ClienteForm, DateProjectForm
from django.views.generic.base import TemplateView



def inicio(request):
    return render (request, "App_ufree/inicio.html")


def Job(request):
    tipo = request.POST.get("tipo")
    id = request.POST.get("id")
    job = Job(nombre=tipo, id=id)
    job.save()
    texto=f"Job Created"
    return HttpResponse(texto)


def Jobs(request):
      if request.method == 'POST':
            FormJobs = JobsForm(request.POST)
            print(FormJobs)
            if FormJobs.is_valid:   
                  info = FormJobs.cleaned_data
                  tipo = info["tipo"]
                  id = info["id"]
                  job = Job(tipo=tipo, id=id)
                  job.save()
                  return render(request,"App_ufree/inicio.html")
      else:
            FormJobs = JobsForm()

      return render(request, "App_ufree/Jobs.html", {"FormJobs":FormJobs})


def Jobs(request):
    return render (request, "App_ufree/Jobs.html")

def Client(request):
      return render(request, "App_ufree/Client.html")

def Clients(request):
      if request.method == 'POST':
            FormClient = ClienteForm(request.POST)
            print(FormClient)
            if FormClient.is_valid:  
                  info = FormClient.cleaned_data
                  client = Client(nombre = info['nombre'], apellido=info['apellido'],email = info['email'], dni = info['dni']) 
                  client.save()
                  return render(request,"App_ufree/inicio.html")

      else: 

            FormJobs= ClienteForm()

      return render(request, "App_ufree/Client.html", {"FormJobs":FormJobs})


def DateProject(request):
      return render(request, "App_ufree/dateproject.html")

def DateProjects(request):
      if request.method == 'POST':
            FormDatePr = DateProjectForm(request.POST)
            print(FormDatePr)
            if FormDatePr.is_valid:  
                  info = FormDatePr.cleaned_data
                  datepr = DateProject(nombre = info['nombre'], apellido=info['apellido'],email = info['email'], dni = info['dni']) 
                  datepr.save()
                  return render(request,"App_ufree/inicio.html")

      else: 

            FormDatePr= DateProjectForm()

      return render(request, "App_ufree/dateproject.html", {"FormJobs":FormJobs})


def search(request):

      if  request.GET["id"]:

            id = request.GET['id'] 
            tipo = Jobs.objects.filter(id__icontains=id)
            return render(request,"App_ufree/inicio.html", {"tipo":tipo, "id":id})

      else:
            answer = "¿Buscas algun dato?"

      return render(request,"App_ufree/search.html", {"respuesta":answer})



def ClientSearch(request):
      clientes = Client.objects.all() 
      contexto = {"Clientes":clientes} 

      return render(request, "App_ufree/ClientSearch.html",contexto)


def DeleteClient(request, nombre_cliente):

      clientes = Client.objects.get(nombre = nombre_cliente)
      clientes.delete()
      clientes = Client.objects.all()
      contexto = {"clientes":clientes} 
      return render(request, "App_ufree/DeleteClient.html",contexto)
