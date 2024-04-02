from django import forms

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


from .models import Curso, Profesor, Alumno

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
