# Proyecto web con python

## Objetivo
Crear una web donde se pueda implementar el funcionamiento model vista template que tiene determinado django, y realizar un CRUD sencillo para distintos objetos(alumnos, profesores, cursos)

## Pasos a seguir
**Clonar el repositorio**
> git clone <url_del_repositorio>

**Instalar librerias usadas**
> pip install -r requirements.txt

**Correr la web en un puerto local en chrome**
> python manage.py runserver


## Disfruta de la web 😁😉

En ella encontraras un sistema de logueo, logout y edicion de usuarios, y cuatro apartados, el de inicio que podra visualizar cualquier persona este o no registrada en la web y otros tres que son:

> ALUMNOS 🧑‍🎓

> PROFESORES 🧑🏻‍🏫

> CURSOS 🎓🗞

Ambos tres los representamos en registros de una base de datos relacional, y usamos un sistema CRUD(create, read, update and delete) en cada uno de los apartados, a los cuales solo va a poder acceder un usuario con los permisos necesarios. Para crear ese tipo de usuario deberas ejecutar "python manage.py createsuperuser" en la terminal.
