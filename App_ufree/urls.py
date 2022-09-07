from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio, name="inicio"),
    path('Job/',Job),
    path('Jobs/', jobs_view, name='MyProjects'),
    path('Client/', Client, name='Clientes'),
    path('DateProject/', DateProject, name = "DateProject"),
    path('JobsForm/', jobs_view, name = "JobsForm"),
    path('ClienteForm/', Clients_view, name = "ClienteForm"),
    path('DateProjectForm/', DateProjects_view, name= 'DateProjectForm' ),
    path('search/', search, name = "search"),
    path('searchresults/', search_id, name = 'searchid')
    ]