from django.urls import path
from App_ufree import views
from .views import inicio
from .forms import forms

urlpatterns = [
   
    path('http://127.0.0.1:8000/', views.inicio, name="Inicio"),
    path("Job/",views.Job),
    path('Jobs', views.Jobs, name="MyProjects"),
    path('Client', views.Client, name="Clientes"),
    path('DateProject', views.DateProject, name="DateProject"),
    path('JobsForm', views.JobsForm, name="JobsForm"),
    path('ClientForm', views.ClienteForm, name="ClientForm"),
    path('search/', views.search),
    path('ClientSearch', views.ClientSearch, name="SearchClient"),
    path('DeleteClient/<nombre_cliente>/', views.DeleteClient, name="EliminarCliente"),

  


  

]

