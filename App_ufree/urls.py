from django.urls import path
#cosas para el login
from django.contrib.auth.views import LogoutView
from App_ufree import views




urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('Type', views.Type, name="TipoProyecto"),
    path('Client', views.Client, name="Clientes"),
    path('DateProject', views.DateProject, name="DateProject"),
    #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    #path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    #path('busquedaCamada',  views.busquedaCamada, name="BusquedaCamada"),
    path('search/', views.search),
    path('ClientSearch', views.ClientSearch, name="SearchClient"),
    path('DeleteClient/<nombre_cliente>/', views.DeleteClient, name="EliminarCliente"),
    path('ClienteEdit/<nombre_cliente>/', views.ClientEdit, name="EditarCliente"),


    path('Type/list', views.TypeList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),



    path('login', views.login_request, name = 'Login'),
    path('register', views.register, name = 'Register'),
    path('logout', LogoutView.as_view(template_name='App_ufree/logout.html'), name = 'Logout'),

    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),


    path('agregarAvatar', views.addavatar, name="AgregarAvatar"),

  


  

]

