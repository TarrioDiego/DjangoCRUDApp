from django.http import HttpResponse
from django.template import Template, Context


def saludar(request):
    return HttpResponse('<h1> Mi primer mensaje </h1>')

def template(request):
    archivo = open('C:/Users/abril/Python/Proyecto_web/plantillas/template.html')
    template= Template(archivo.read())
    archivo.close()

    contexto = Context({'nombre':'Diego'})

    documento = template.render(contexto)

    return HttpResponse(documento)
