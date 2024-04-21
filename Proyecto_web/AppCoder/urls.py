from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('altaCurso<nombre>',alta_curso),
    path("", inicio, name='inicio'),
    path('cursos', ver_cursos, name='cursos'),
    path('agregar_curso', curso_formulario, name='agregar_curso'),
    path('buscar_curso',buscar_curso, name='buscar_curso'),
    path('eliminar_curso/<int:id>', eliminar_curso, name='eliminar_curso'),
    path('editar_curso<int:id>', editar_curso , name='editar_curso'),


    path('profesores', profesores, name='profesores'),
    path('agregar_profesor', profesor_formulario, name='agregar_profesor'),
    path('eliminar_profesor/<int:id>', eliminar_profesor, name='eliminar_profesor'),
    path('editar_profesor<int:id>', editar_profesor, name='editar_profesor'),
    path('buscar_profesor', buscar_profesor, name='buscar_profesor'),

    path("alumnos", alumnos , name="alumnos"),
    path('agregar_alumno', alumno_formulario, name='agregar_alumno'),
    path('eliminar_alumno/<int:id>', eliminar_alumno, name='eliminar_alumno'),
    path('editar_alumno<int:id>', editar_alumno, name='editar_alumno'),
    path('buscar_alumno', buscar_alumno, name='buscar_alumno'),

    path('login', login_request, name='login'),
    path('register', register, name='register'),
    path('logout', LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('editarperfil', editar_perfil, name='editar_perfil')

]
