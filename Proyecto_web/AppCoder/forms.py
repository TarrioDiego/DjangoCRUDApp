from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
'''
class Curso_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()   
    profesor_de_la_catedra = forms.ChoiceField(queryset=Profesor.objects.all())

class ProfesorForm(forms.Form):

    nombre = forms.CharField(max_length=70)
    apellido = forms.CharField(max_length=70)
    email = forms.EmailField()
    

class AlumnosForm(forms.Form):

    nombre = forms.CharField(max_length=70)
    apellido = forms.CharField(max_length=70)
    curso = forms.ChoiceField(queryset=Curso.objects.all())
    mail = forms.EmailField()
    
'''  # Otra forma de armar los forms


from .models import Curso, Profesor, Alumno, Avatar

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'camada', 'profesor_de_la_catedra']

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'mail']

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'curso', 'mail']
        widgets = {'curso': forms.CheckboxSelectMultiple}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Agregar/modificar Email:")
    password1 = forms.CharField(label="Contrasenia", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contrasenia", widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','password1','password2']
        help_text = {k:"" for k in fields}

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']