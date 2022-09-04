from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Jobs(models.Model):

    tipo = models.CharField(max_length=40)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return f"Tipo del Proyecto: {self.tipo} - {self.id}"

class Client(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    email = models.EmailField()
    dni = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - DNI {self.dni}"

class DateProject(models.Model):
    first_deliver = models.DateTimeField()
    second_deliver = models.DateTimeField()
    delivered = models.BooleanField()


    def __str__(self):
        return f"First Deliver: {self.first_deliver} - Second Deliver {self.second_deliver} - delivered {self.delivered}"