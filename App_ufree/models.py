from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Type(models.Model):

    tipo = models.CharField(max_length=40)
    id = models.IntegerField()

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
    deliver = models.BooleanField()

class Avatar(models.Model):
    #vinvulo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #Subcaperta avatares de media :) 
    picture = models.ImageField(upload_to = 'avatares', blank = True, null=True)

    def __str__(self):
        return f"Imagen de: {self.user.username}"

   
def get_image_filename(instance, filename):
    title =  'titulo'
    slug = slugify(title)
    return "imagenesAvatares/%s-%s" % (slug, filename)  


