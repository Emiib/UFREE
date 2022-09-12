from django.db import models

class Jobs(models.Model):

    tipo = models.CharField(max_length=40)
    num = models.IntegerField(default="0")

    def __str__(self):
        return f"Project type: {self.tipo} - num {self.num}"
class Client(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    email = models.EmailField()
    dni = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Dni {self.dni}"

class DateProject(models.Model):
    first_deliver = models.DateTimeField()
    second_deliver = models.DateTimeField()
    delivered = models.BooleanField()

    def __str__(self):
        return f"First Deliver: {self.first_deliver} - Second Deliver {self.second_deliver} - delivered {self.delivered}"