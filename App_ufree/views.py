from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from .models import Jobs, Client, DateProject
from .forms import JobsForm, ClienteForm, DateProjectForm

def inicio(request):
    return render (request, "inicio.html")





def Job(request):
      tipo = request.POST.get("tipo")
      num = request.POST.get("num")
      Job = Jobs(tipo=tipo, num=num)
      Job.save()
def jobs_view(request):
      if request.method == 'POST':
            formulario = JobsForm(request.POST)
            print(formulario)
            if formulario.is_valid():  
                  info = formulario.cleaned_data
                  tipo = info["tipo"]
                  num = info["num"]
                  Job = Jobs(tipo=tipo,num=num)
                  Job.save()
                  return render(request, "Jobs.html",{"formulario":formulario})
      else:
            formulario = JobsForm()
            
      return render(request, "Jobs.html", {"formulario":formulario})
      



def clienty(request):
      nombre = request.POST.get("nombre")
      apellido = request.POST.get("apellido")
      email = request.POST.get("email")
      dni = request.POST.get("dni")
      clienty = Client(nombre=nombre, apellido=apellido, email = email, dni=dni)
      clienty.save()
def Clients_view(request):
      if request.method == 'POST':
            formulario = ClienteForm(request.POST)
            print(formulario)
            if formulario.is_valid():  
                  info = formulario.cleaned_data
                  nombre = info["nombre"]
                  apellido = info["apellido"]
                  email = info["email"]
                  dni = info["dni"]
                  clienty = Client(nombre=nombre, apellido=apellido, email= email, dni = dni) 
                  clienty.save()
                  texto="Client created"
                  return HttpResponse(texto)
      else: 
            formulario = ClienteForm()
      
      return render(request, "Client.html", {"formulario":formulario})




def datepr(request):
    first_deliver = request.POST.get("first_deliver")
    second_deliver = request.POST.get("second_deliver")
    delivered = request.POST.get("delivered")
    datepr = DateProject(first_deliver=first_deliver, second_deliver=second_deliver, delivered = delivered)
    datepr.save()
def DateProjects_view(request):
      if request.method == 'POST':
            formulario = DateProjectForm(request.POST)
            print(formulario)
            if formulario.is_valid():
                  info = formulario.cleaned_data
                  first_deliver = info["first_deliver"]
                  second_deliver = info["second_deliver"]
                  delivered = info["delivered"]
                  datepr = DateProject(first_deliver = first_deliver, second_deliver=second_deliver,delivered = delivered) 
                  datepr.save()
                  texto="Date Updated"
                  return HttpResponse(texto)
      else: 
            formulario = DateProjectForm()
            return render(request, "dateproject.html", {"formulario":formulario})


def searchresults(request):
      return render(request, "searchresults.html")

def search(request):
      if request.GET.get("num"):
        num = request.GET.get("num")
        Job = Jobs.objects.filter(num__icontains = num)
        return render(request, "searchresults.html", {"Job":Job, "num":num})
      else:
        return render(request, "search.html", {"notification":"Please, enter a number"})