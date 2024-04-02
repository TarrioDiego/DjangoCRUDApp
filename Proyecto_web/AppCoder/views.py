from django.shortcuts import render 
from AppCoder.models import Curso, Profesor, Alumno
from django.http import HttpResponse 
from django.template import loader
from AppCoder.forms import CursoForm, ProfesorForm , AlumnoForm
# Create your views here.


def inicio(request):
    return render(request, 'padre.html')

#  --------- Inicio Apartado views sobre cursos ----------------------
def alta_curso(request,nombre):
    curso = Curso(nombre=nombre, camada=234567)
    curso.save()

    texto = f'Se guardo el curso: {curso.nombre} {curso.camada}'
    return render(request, 'formulario.html')
    


def ver_cursos(request):
    cursos = Curso.objects.all() # devuelve una lista de diccionarios
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def curso_formulario(request):
    
    if request.method == 'POST':

        mi_formulario = CursoForm(request.POST)
        print(mi_formulario)
        

        if mi_formulario.is_valid(): 
            datos = mi_formulario.cleaned_data 
            curso = Curso(nombre=datos['nombre'], camada=datos['camada'])
            curso.save()
        return ver_cursos(request)
    mi_formulario = CursoForm()
    return render(request, 'formulario.html', context={'mi_formulario':mi_formulario})

def buscar_curso(request):
    if request.method =="POST":
        nombre = request.POST['nombre']
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render(request,'cursos.html',context={'cursos':cursos})

    else:
        return render(request,'buscar_curso.html')


def eliminar_curso(request,id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    # Vuelvo al menu
    curso=Curso.objects.all() # Trae todos los cursos

    return render(request,'cursos.html', context={'cursos':curso} )

def editar_curso(request, id):
    
    curso = Curso.objects.get(id=id)
    if request.method == 'POST':
        formulario = CursoForm(request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data

            curso.nombre = info['nombre']
            curso.camada = info['camada']

            curso.save()

            curso = Curso.objects.all()

            return render(request, 'cursos.html', {'cursos':curso})
      
        
    else:
        form_con_datos= CursoForm(initial={'nombre': curso.nombre, 'camada': curso.camada})
       
    return render(request, 'editarform.html', context={'mi_formulario':form_con_datos, 'curso':curso})

# ---------------- Fin apartado views sobre cursos ----------------------------
  

def profesores(request):
    profesores = Profesor.objects.all()# devuelve una lista de diccionarios
    return render(request, 'profesores.html', context={'profesores': profesores})


def profesor_formulario(request):
    
    if request.method == 'POST':

        mi_formulario = ProfesorForm(request.POST)
        print(mi_formulario)
        

        if mi_formulario.is_valid(): 
            datos = mi_formulario.cleaned_data 
            curso = Profesor(nombre=datos['nombre'], apellido=datos['apellido'], mail=datos['mail'])
            curso.save()
        return profesores(request)
    mi_formulario = ProfesorForm()
    return render(request, 'profesform.html', context={'mi_formulario':mi_formulario})



def eliminar_profesor(request,id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()

    # Vuelvo al menu
    profesores = Profesor.objects.all() # Trae todos los cursos

    return render(request,'profesores.html', context={'profesores':profesores} )


def editar_profesor(request, id):
    
    profesor = Profesor.objects.get(id=id)
    if request.method == 'POST':
        formulario = ProfesorForm(request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data

            profesor.nombre = info['nombre']
            profesor.apellido = info['apellido']
            profesor.mail = info['mail']

            profesor.save()

            profesores = Profesor.objects.all()

            return render(request, 'profesores.html', {'profesores':profesores})
      
        
    else:
        form_con_datos= ProfesorForm(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido, 'mail': profesor.mail})
       
    return render(request, 'profeseditarform.html', context={'mi_formulario':form_con_datos, 'profesor':profesor})

def buscar_profesor(request):
    if request.method =="POST":
        nombre = request.POST['nombre']
        profesores = Profesor.objects.filter(nombre__icontains=nombre)
        return render(request,'profesores.html',context={'profesores':profesores})

    else:
        return render(request,'buscar_profesor.html')

# ---------------- Inicio apartado views sobre alumnos -------------------------


def alumnos(request):
    alumnos = Alumno.objects.all()# devuelve una lista de diccionarios
    return render(request, 'alumnos.html', context={'alumnos': alumnos})


def alumno_formulario(request):
    
    if request.method == 'POST':

        mi_formulario = AlumnoForm(request.POST)
        print(mi_formulario)
        

        if mi_formulario.is_valid(): 
            datos = mi_formulario.cleaned_data 
            alumno = Alumno(nombre=datos['nombre'], apellido=datos['apellido'],mail=datos['mail'])
            alumno.save()
            cursos_seleccionados = mi_formulario.cleaned_data['curso']
            alumno.curso.set(cursos_seleccionados)
            alumno.save()
        return alumnos(request)
    mi_formulario = AlumnoForm()
    return render(request, 'alumnosform.html', context={'mi_formulario':mi_formulario})



def eliminar_alumno(request,id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()

    # Vuelvo al menu
    alumnos = Alumno.objects.all() # Trae todos los cursos

    return render(request,'alumnos.html', context={'alumnos':alumnos} )


def editar_alumno(request, id):
    
    alumno = Alumno.objects.get(id=id)
    if request.method == 'POST':
        formulario = AlumnoForm(request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data

            alumno.nombre = info['nombre']
            alumno.apellido = info['apellido']
            alumno.mail = info['mail']

            alumno.save()
            cursos_seleccionados = formulario.cleaned_data['curso']
            alumno.curso.set(cursos_seleccionados)
            alumno.save()

            alumnos = Alumno.objects.all()

            return render(request, 'alumnos.html', {'alumnos':alumnos})
      
        
    else:
        cursos_actuales = alumno.curso.all()
        form_con_datos= AlumnoForm(initial={'nombre': alumno.nombre, 'apellido': alumno.apellido, 'curso':cursos_actuales, 'mail': alumno.mail})
       
    return render(request, 'alumnoseditarform.html', context={'mi_formulario':form_con_datos, 'alumno':alumno})

def buscar_alumno(request):
    if request.method =="POST":
        nombre = request.POST['nombre']
        alumnos = Alumno.objects.filter(nombre__icontains=nombre)
        return render(request,'alumnos.html',context={'alumnos':alumnos})

    else:
        return render(request,'buscar_alumno.html')
