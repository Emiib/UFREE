from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',inicio, name="inicio"),
    
    path('Job/',Job),
    path('clientss/', clientss),
    path('datepr/', datepr),

    path('Jobs/', jobs_view, name='jobsview'),
    path('Client/', Clients_view, name='Clients_view'),
    path('DateProject/', DateProjects_view, name = "DateProjects_view"),

    path('JobsForm/', jobs_view, name = "jobs_view"),
    path('ClienteForm/', Clients_view, name = "Clients_view"),
    path('DateProjectForm/', DateProjects_view, name= 'DateProjects_view' ),

    path('searchresults/', searchresults, name = "searchresults"),
    path('search/', search, name= "search"),

    path('readclient/', readclient, name="readclient"),
    path('delclient/<id>', delclient, name='delclient'),
    path('editclient/<id>', editclient, name='editclient'),

    path('login/', login_request, name = "login"),
    path('register/', register, name = "register"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    ]