from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio, name="inicio"),
    
    path('Job/',Job),
    path('clientss/', clientss),
    path('datepr/', datepr),

    path('Jobs/', jobs_view, name='jobsview'),
    path('Client/', Clients_view, name='clientsview'),
    path('DateProject/', DateProjects_view, name = "DateProjectsview"),

    path('JobsForm/', jobs_view, name = "JobsForm"),
    path('ClienteForm/', Clients_view, name = "ClienteForm"),
    path('DateProjectForm/', DateProjects_view, name= 'DateProjectForm' ),

    path('searchresults/', searchresults, name = "searchresults"),
    path('search/', search, name= "search"),

    path("readclient/", readclient, name="ReadClient"),
    path('delclient/<id>', delclient, name='DelClient'),
    path('editclient/<id>', editclient, name='EditClient'),
    
    ]