from django.shortcuts import render 
from AppCoder.models import Curso, Profesor, Alumno, Avatar
from django.http import HttpResponse 
from django.template import loader
from AppCoder.forms import CursoForm, ProfesorForm , AlumnoForm, UserEditForm, AvatarForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required 
from django.contrib.auth import update_session_auth_hash 
# Create your views here.


def mostrar_avatar(request):
    if request.user.is_authenticated:
        avatares = Avatar.objects.filter(user=request.user.id)
        if avatares:
            return avatares[0].imagen.url
    return None

def inicio(request):
    return render(request, 'index.html', {'url':mostrar_avatar(request)})

#  --------- Inicio Apartado views sobre cursos ----------------------
def alta_curso(request,nombre):
    curso = Curso(nombre=nombre, camada=234567)
    curso.save()

    texto = f'Se guardo el curso: {curso.nombre} {curso.camada}'
    return render(request, 'formulario.html')
    

@login_required
def ver_cursos(request):
    cursos = Curso.objects.all() # devuelve una lista de diccionarios
   # plantilla = loader.get_template("cursos.html")
   # documento = plantilla.render(dicc)
    #avatares = Avatar.objects.filter(user=request.user.id)
    #url_avatar = mostrar_avatar(request)
    return render(request,'cursos.html', context={"cursos": cursos,'url':mostrar_avatar(request) })


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
    return render(request, 'formulario.html', context={'mi_formulario':mi_formulario ,'url':mostrar_avatar(request)})

def buscar_curso(request):
    if request.method =="POST":
        nombre = request.POST['nombre']
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render(request,'cursos.html',context={'cursos':cursos,'url':mostrar_avatar(request)})

    else:
        return render(request,'buscar_curso.html', {'url':mostrar_avatar(request)})


def eliminar_curso(request,id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    # Vuelvo al menu
    curso=Curso.objects.all() # Trae todos los cursos

    return render(request,'cursos.html', context={'cursos':curso ,'url':mostrar_avatar(request)} )

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

            return render(request, 'cursos.html', {'cursos':curso ,'url':mostrar_avatar(request)})
      
        
    else:
        form_con_datos= CursoForm(initial={'nombre': curso.nombre, 'camada': curso.camada})
       
    return render(request, 'editarform.html', context={'mi_formulario':form_con_datos, 'curso':curso ,'url':mostrar_avatar(request)})

# ---------------- Fin apartado views sobre cursos ----------------------------
  
@login_required
def profesores(request):
    profesores = Profesor.objects.all()# devuelve una lista de diccionarios
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'profesores.html', context={"url":avatares[0].imagen.url,'profesores': profesores})


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
    return render(request, 'profesform.html', context={'mi_formulario':mi_formulario,'url':mostrar_avatar(request)})



def eliminar_profesor(request,id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()

    # Vuelvo al menu
    profesores = Profesor.objects.all() # Trae todos los cursos

    return render(request,'profesores.html', context={'profesores':profesores,'url':mostrar_avatar(request)} )


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

            return render(request, 'profesores.html', {'profesores':profesores,'url':mostrar_avatar(request)})
      
        
    else:
        form_con_datos= ProfesorForm(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido, 'mail': profesor.mail})
       
    return render(request, 'profeseditarform.html', context={'mi_formulario':form_con_datos, 'profesor':profesor,'url':mostrar_avatar(request)})

def buscar_profesor(request):
    if request.method =="POST":
        nombre = request.POST['nombre']
        profesores = Profesor.objects.filter(nombre__icontains=nombre)
        return render(request,'profesores.html',context={'profesores':profesores ,'url':mostrar_avatar(request)})

    else:
        return render(request,'buscar_profesor.html',{'url':mostrar_avatar(request)})

# ---------------- Inicio apartado views sobre alumnos -------------------------

@login_required
def alumnos(request):
    alumnos = Alumno.objects.all()# devuelve una lista de diccionarios
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'alumnos.html', context={"url":avatares[0].imagen.url,'alumnos': alumnos})


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
    return render(request, 'alumnosform.html', context={'mi_formulario':mi_formulario,'url':mostrar_avatar(request)})



def eliminar_alumno(request,id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()

    # Vuelvo al menu
    alumnos = Alumno.objects.all() # Trae todos los cursos

    return render(request,'alumnos.html', context={'alumnos':alumnos ,'url':mostrar_avatar(request)} )


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

            return render(request, 'alumnos.html', {'alumnos':alumnos,'url':mostrar_avatar(request)})
      
        
    else:
        cursos_actuales = alumno.curso.all()
        form_con_datos= AlumnoForm(initial={'nombre': alumno.nombre, 'apellido': alumno.apellido, 'curso':cursos_actuales, 'mail': alumno.mail})
       
    return render(request, 'alumnoseditarform.html', context={'mi_formulario':form_con_datos, 'alumno':alumno})

def buscar_alumno(request):
    if request.method =="POST":
        nombre = request.POST['nombre']
        alumnos = Alumno.objects.filter(nombre__icontains=nombre)
        return render(request,'alumnos.html',context={'alumnos':alumnos,'url':mostrar_avatar(request)})

    else:
        return render(request,'buscar_alumno.html',context={'url':mostrar_avatar(request)})



# ---------------- Inicio apartado login y logout ----------------------

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data= request.POST)

        if form.is_valid():
            usuario = form.cleaned_data['username']
            contra = form.cleaned_data['password']

            user = authenticate(username= usuario, password=contra)
            

            if user is not None:
                login(request , user)
                avatares = Avatar.objects.filter(user=request.user.id)
                if avatares.exists() and avatares[0].imagen:
                    url_avatar = avatares[0].imagen.url
                else:
                    url_avatar = None
            
                return render(request, 'index.html', {"url":url_avatar, 'mensaje': f'bienvenido/a {usuario}' })

        
            else:
                return render(request,'index.html',{'mensaje':f'usuario no encontrado'})
        
        else:
            return render(request,'index.html',{'mensaje':f"FORMULARIO INCORRECTO  {form}"})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html',{'form': form})


def register(request):
    

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = "Usuario creado"
            return render(request,'index.html',{'mensaje': mensaje})
        else:
            mensaje = "Error en la ingesta de datos"
            return render(request,'index.html',{'mensaje': mensaje})
    else:
        form = UserCreationForm()
        return render(request, 'registro.html', {'form':form})

@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == 'POST':
        mi_formulario = UserEditForm(request.POST)

        avatar_form = AvatarForm(request.POST, request.FILES)
        

        if mi_formulario.is_valid(): # Si los datos ingresados son correctos
            
            informacion = mi_formulario.cleaned_data
            usuario.email = informacion['email']
            password = informacion['password1']
            usuario.set_password(password)
            usuario.save()

        if avatar_form.is_valid():
            avatar_viejo = Avatar.objects.filter(user=usuario).first() # .first() toma el primer objeto del queryset resultante. Si no hay ningún objeto en el queryset, first() devolverá None.
            if avatar_viejo:
                
                avatar_viejo.delete()
            
            avatar_instance = avatar_form.save(commit=False)
            avatar_instance.user = usuario
            avatar_instance.save()    
            update_session_auth_hash(request, usuario) # Se utiliza para mantener la seccion activa y no tener que loguearse
            return render(request, 'index.html', {'url':mostrar_avatar(request)})

    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})
        avatar_form = AvatarForm()
    return render(request , "editar_perfil.html", {"miFormulario":miFormulario, 'avatar_form': avatar_form,"usuario":usuario,'url':mostrar_avatar(request)})
