from django import forms

class JobsForm(forms.Form):
    tipo = forms.CharField(max_length=100)
    id = forms.IntegerField()

class ClienteForm(forms.Form):   
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    dni = forms.IntegerField()

class DateProjectForm(forms.Form):
    first_deliver = forms.DateTimeField()
    second_deliver = forms.DateTimeField()
    delivered = forms.BooleanField()