from django.urls import path
from App_ufree.views import *

urlpatterns = [
    path('http://127.0.0.1:8000/', inicio, name="Inicio"),
    path("Job/",Job),

    path('Jobs/', Jobs, name="MyProjects"),
    path('Client/', Client, name="Clientes"),
    path('DateProject/', DateProject, name = "DateProject"),
    path('JobsForm/', JobsForm, name = "JobsForm"),
    path('ClientForm/', ClienteForm, name = "ClientForm"),
    path('search/', search, name = "search"),
    path('ClientSearch/', ClientSearch, name="SearchClient"),
    path('DeleteClient/<nombre_cliente>/', DeleteClient, name="EliminarCliente"),
    ]