from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

class JobsForm(forms.Form):
    tipo = forms.CharField(max_length=100)
    num = forms.IntegerField()

class ClienteForm(forms.Form):   
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    dni = forms.IntegerField()

class DateProjectForm(forms.Form):
    first_deliver = forms.DateTimeField()
    second_deliver = forms.DateTimeField()
    delivered = forms.BooleanField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password_1= forms.CharField(label="Enter your password", widget=forms.PasswordInput)
    password_2= forms.CharField(label="Repit your password, please", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password_1', 'password_2']
        help_texts = {k:"" for k in fields}
