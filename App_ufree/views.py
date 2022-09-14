from django.shortcuts import render
from django.http import HttpResponse

from .models import Jobs, Client, DateProject
from .forms import JobsForm, ClienteForm, DateProjectForm, UserRegisterForm

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required


def inicio(request):
    return render (request, "inicio.html")




@login_required
def Job(request):
      tipo = request.POST.get("tipo")
      num = request.POST.get("num")
      Job = Jobs(tipo=tipo, num=num)
      Job.save()
@login_required
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
                  return render(request, "JobsForm.html",{"formulario":formulario})
      else:
            formulario = JobsForm()
            return render(request, "JobsForm.html", {"formulario":formulario})
      

@login_required
def clientss(request):
    return render (request, "clientss.html")
@login_required
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
                  clientss=Client.objects.all()
                  return render(request, "readclient.html", {"clientss":clientss})
      else: 
            formulario = ClienteForm()
      return render(request, "Client.html", {"formulario":formulario})

#profesores = clientss
#profe = clienty
#profesor = clients_s
@login_required
def readclient(request):
    clientss=Client.objects.all()
    print(list(clientss))
    return render(request, "readclient.html", {"clientss":clientss})
@login_required
def delclient(request, id):
    client_s=Client.objects.get(id=id)
    client_s.delete()
    clientss=Client.objects.all()
    return render(request, "readclient.html", {"clientss":clientss})
@login_required
def editclient(request, id):
    clients_s=Client.objects.get(id=id)
    if request.method=="POST":
        formulario=ClienteForm(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            clients_s.nombre=info["nombre"]
            clients_s.apellido=info["apellido"]
            clients_s.email=info["email"]
            clients_s.dni=info["dni"]
            clients_s.save()
            clients_s=Client.objects.all()
            return render(request, "readclient.html", {"clientss":clientss})
    else:
        formulario= ClienteForm(initial={"nombre":clients_s.nombre, "apellido":clients_s.apellido, "email":clients_s.email, "dni":clients_s.dni})
        return render(request, "editclient.html", {"formulario":formulario, "clients_s":clients_s})

@login_required
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

@login_required
def searchresults(request):
      return render(request, "searchresults.html")
@login_required
def search(request):
      if request.GET.get("num"):
        num = request.GET.get("num")
        Job = Jobs.objects.filter(num__icontains = num)
        return render(request, "searchresults.html", {"Job":Job, "num":num})
      else:
        return render(request, "search.html", {"notification":"Please, enter a number"})


def login_request(request):
    if request.method=="POST":
        formulario=AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            user=request.POST["username"]
            passw=request.POST["password"]
            User=authenticate(username=user, password=passw)
            if User is not None:
                login(request, User)
                return render(request, 'inicio.html', {'mensaje':f"Nice to see you again {User}"})
            else:
                return render(request, "login.html", {"formulario":formulario, "mensaje":"Username or password incorrect"})
        else:
            return render(request, "login.html", {"formulario":formulario, "mensaje":"Username or password incorrect"})              
    else:
        formulario=AuthenticationForm()
        return render(request, "login.html", {"formulario":formulario})

def register(request):
    if request.method=="POST":
        formulario=UserRegisterForm(request.POST)
        if formulario.is_valid():
            username=formulario.cleaned_data.get('username')
            formulario.save()
            return render(request, "inicio.html", {"mensaje":f"Welcome {username}, it's nice to meet you"})
        else:
            return render(request, "register.html", {"formulario":formulario, "mensaje":"FORMULARIO INVALIDO"})

    else:
        formulario=UserRegisterForm()
        return render(request, "register.html", {"formulario":formulario})


