from django.urls import path
from App_ufree import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path("Job/",views.Job),
    path('Jobs', views.Jobs, name="MyProjects"),
    path('Client', views.Client, name="Clientes"),
    path('DateProject', views.DateProject, name="DateProject"),
    #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    #path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    #path('busquedaCamada',  views.busquedaCamada, name="BusquedaCamada"),
    path('search/', views.search),
    path('ClientSearch', views.ClientSearch, name="SearchClient"),
    path('DeleteClient/<nombre_cliente>/', views.DeleteClient, name="EliminarCliente"),

  


  

]

