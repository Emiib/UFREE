from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio),
    path('Job/',Job),
    path('Jobs/', Jobs, name='MyProjects'),
    path('Client/', Client, name='Clientes'),
    path('DateProject/', DateProject, name = "DateProject"),
    path('JobsForm/', JobsForm, name = "JobsForm"),
    path('ClientForm/', ClienteForm, name = "ClientForm"),
    path('search/', search, name = "search"),
    ]