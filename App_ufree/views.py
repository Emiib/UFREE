from django.shortcuts import redirect, render, HttpResponse
from typing import List
from django.http import HttpResponse
from App_ufree.models import Type, Client, DateProject, Avatar
from App_ufree.forms import TypeForm, ClienteForm, DateProjectForm, UserRegisterForm, UserEditForm, AvatarForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

#Para la prueba unitaria
import string
import random

#Para el login

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

#Decorador por defecto
from django.contrib.auth.decorators import login_required

from django.views.generic.base import TemplateView

@login_required

def inicio(request):
      avatares = Avatar.objects.filter(user=request.user.id)
      return render(request, "App_ufree/inicio.html", {"url":avatares[0].imagen.url})


def Type(request):
      id =  id(nombre="App Inmobiliaria", id = "3000")
      id.save()
      Datatxt = f"Type: {id.nombre} ID: {id.id}"
      return HttpResponse(Datatxt)


def Client(request):
      return render(request, "App_ufree/Client.html")


def DateProject(request):
      return render(request, "App_ufree/dateproject.html")


def Type(request):
      if request.method == 'POST':
            FormType = TypeForm(request.POST)
            print(FormType)
            if FormType.is_valid:   
                  info = FormType.cleaned_data
                  id = id (nombre=info['id'], id = info['ID']) 
                  id.save()
                  return render(request,"App_ufree/inicio.html")

      else:
            FormType = TypeForm()

      return render(request, "App_ufree/type.html", {"FormType":FormType})


def Client(request):
      if request.method == 'POST':
            FormType = ClienteForm(request.POST)
            print(FormType)
            if FormType.is_valid:  
                  info = FormType.cleaned_data
                  cliente = cliente (nombre = info['nombre'], apellido=info['apellido'],
                  email=info['email'], dni = info['dni']) 
                  cliente.save()
                  return render(request,"App_ufree/inicio.html")

      else: 

            FormType= ClienteForm()

      return render(request, "App_ufree/Client.html", {"FormType":FormType})



def search(request):

      if  request.GET["id"]:

	      #respuesta = f"Estoy buscando la id nro: {request.GET['id'] }" 
            id = request.GET['id'] 
            tipo = type.objects.filter(id__icontains=id)
            return render(request,"App_ufree/inicio.html", {"tipo":tipo, "id":id})

      else:
            answer = "¿Buscas algun dato?"

      return render(request,"App_ufree/inicio.html", {"respuesta":answer})



def ClientSearch(request):
      clientes = Client.objects.all() 
      contexto = {"Clientes":clientes} 

      return render(request, "App_ufree/ClientSearch.html",contexto)



def DeleteClient(request, nombre_cliente):

      clientes = Client.objects.get(nombre = nombre_cliente)
      clientes.delete()
      #vuelvo al menú
      clientes = Client.objects.all() #trae todos los profesores
      contexto = {"clientes":clientes} 
      return render(request, "App_ufree/DeleteClient.html",contexto)



def ClientEdit(request, nombre_cliente):

      #Recibe el nombre del cliente que vamos a modificar
      clientes = Client.objects.get(nombre = nombre_cliente)

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':
            FormType = ClienteForm(request.POST)
            print(FormType)
            if FormType.is_valid:

                  info = FormType.cleaned_data

                  clientes.nombre = info['nombre']
                  clientes.apellido = info['apellido']
                  clientes.email = info['email']
                  clientes.dni = info['dni']
                  clientes.save()

                  return render(request, "App_ufree/inicio.html")
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            FormType= ClienteForm(initial={'nombre': clientes.nombre, 'apellido':clientes.apellido , 
            'email':clientes.email, 'dni':clientes.dni}) 

      #Voy al html que me permite editar
      return render(request, "App_ufree/editarcliente.html", {"FormType":FormType, "nombre_cliente":nombre_cliente})




class TyleList(ListView):

      model = Type 
      template_name = "App_ufree/Types_list.html"

class TypeDetalle(DetailView):

      model = Type
      template_name = "App_ufree/Type_detalle.html"

class TypeCreacion(CreateView):

      model = Type
      success_url = "/App_ufree/Type/list"
      fields = ['nombre', 'id']


class TypeUpdate(UpdateView):

      model = Type
      success_url = "/App_ufree/Type/list"
      fields  = ['nombre', 'id']


class TypeDelete(DeleteView):

      model = Type
      success_url = "/App_ufree/Type/list"




def logout_request(request):
      logout(request)
     
      return redirect("inicio")
     

def login_request(request):


      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  password = form.cleaned_data.get('password')

                  user = authenticate(username = usuario, password = password)

            
                  if user is not None:
                        login(request, user)
                       
                        return render(request,"App_ufree/inicio.html",  {"mensaje":f"Que bueno verte {usuario}"} )
                  else:
                        
                        return render(request,"App_ufree/inicio.html", {"mensaje":"Intente nuevamente, por favor"} )

            else:
                        
                        return render(request,"App_ufree/inicio.html" ,  {"mensaje":"Error en el formulario"})

      form = AuthenticationForm()

      return render(request,"App_ufree/login.html", {'form':form} )



def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"App_ufree/Clientl" ,  {"mensaje":"Usuario Creado :)"})


      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"App_ufree/Clienttml" ,  {"form":form})



@login_required
def editarPerfil(request):

      #Instancia del login
      usuario = request.user
     
      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':
            FormType = UserEditForm(request.POST) 
            if FormType.is_valid:   #Si pasó la validación de Django

                  info = FormType.cleaned_data
            
                  #Datos que se modificarán
                  usuario.email = info['email']
                  usuario.password1 = info['password1']
                  usuario.password2 = info['password1']
                  usuario.save()

                  return render(request, "App_ufree/Clientl") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            FormType= UserEditForm(initial={ 'email':usuario.email}) 

      #Voy al html que me permite editar
      return render(request, "App_ufree/Clientil.html", {"FormType":FormType, "usuario":usuario})



@login_required
def addavatar(request):
      if request.method == 'POST':

            FormType = AvatarForm(request.POST, request.FILES) #aquí mellega toda la información del html

            if FormType.is_valid:   #Si pasó la validación de Django
                  u = User.objects.get(username=request.user)
                  avatar = Avatar (user=u, imagen=FormType.cleaned_data['imagen']) 
                  avatar.save()
                  return render(request, "App_ufree/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            FormType= AvatarForm() #Formulario vacio para construir el html

      return render(request, "App_ufree/addavatar.html", {"FormType":FormType})

def urlImagen():
      return "/media/avatares/logo.png"
