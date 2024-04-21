from django.db import models
from django.contrib.auth.models import User     
# Create your models here.


class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    profesor_de_la_catedra= models.ForeignKey('Profesor', on_delete=models.CASCADE, related_name="Cursos",default=None, null=True) #related_name permite acceder desde un objeto profesor a sus respectivos cursos ej: profe1.cursos.all()

    def __str__(self) -> str:
        return f'Nombre: {self.nombre} --  Camada: {self.camada}'


class Profesor(models.Model):

    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=70)
    mail = models.EmailField()

    def __str__(self) -> str:
        return f'Nombre: {self.nombre} -- Apellido: {self.apellido} -- Curso: {self.Cursos}'

class Alumno(models.Model):

    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=70)
    curso = models.ManyToManyField(Curso, related_name='Alumnos') #en una relacion de muchos a muchos no hace falta definir on_delete
    mail = models.EmailField()

    def __str__(self) -> str:
        return f'Nombre: {self.nombre} -- Apellido: {self.apellido}'
    

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)