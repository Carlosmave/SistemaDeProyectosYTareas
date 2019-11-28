from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Proyecto, Tarea
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def form_login(request):
    return render(request, 'projectxapp/login.html')

def auth_login(request):

    usuario = request.POST['usuario']
    clave = request.POST['password']

    u = authenticate(username=usuario, password=clave)

    if u is None:
        return HttpResponseRedirect(reverse('e404'))
    else:
        login(request, u)
        return HttpResponseRedirect(reverse('inicio'))

def crear_cuenta(request):
    if (request.method == 'POST' and 'registrar' in request.POST):
        username=request.POST.get('username', '')
        email=request.POST.get('inputemail', '')
        password=request.POST.get('password', '')
        user_obj = User(username=username, password=password, email=email)
        user_obj.save()
        return render(request, 'projectxapp/login.html')
    else:
        return render(request, 'projectxapp/register.html')

def forgot_password(request):
    return render(request, 'projectxapp/forgot_password.html')

def e404(request):
    return render(request, 'projectxapp/404.html')


def auth_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('form_login'))

@login_required
def inicio(request):
    return render(request, 'projectxapp/inicio.html')
####################################PROYECTOS###################################
@login_required
def proyectos(request):
    #Obtiene los nombres de los proyectos de la base de datos
    pryts = Proyecto.objects.all()
    #Agrega los proyectos al contexto
    contexto = {
        'proyectos': pryts
    }
    #Muestra el template enviando el contexto
    return render(request, 'projectxapp/MisProyectos.html', contexto)

@login_required
def form_proyectos(request):
    return render(request, 'projectxapp/form_proyectos.html')


@login_required
def crear_proyecto(request):
     return HttpResponseRedirect(reverse('proyectos'))

####################################TAREAS###################################

@login_required
def tareas(request):
    #Obtiene
    t = Tarea.objects.all()
    #Agrega
    contexto = {
        'tareas': t
    }
    #Muestra
    return render(request, 'projectxapp/MisTareas.html', contexto)

@login_required
def form_tareas(request):
    pyrs = Proyecto.objects.all()
    contexto={
        'proyectos': pyrs
    }
    return render(request, 'projectxapp/form_tareas.html', contexto)


@login_required
def crear_tarea(request):
    # #Obtiene el nombre digitado por el usuario
    # titulo = request.POST['nombre_tarea']
    # proyecto_id = request.POST['']
    # desarrolladores =  request.POST['']
    # #Obtiene el id del proyecto de la tarea
    # proyecto_id = Tarea.objects.get(pk=int(tarea_id)) ###Esta linea no estoy seguro
    # #Crea la tarea
    # t = Tarea()
    # t.titulo = titulo
    # t.activo = True
    # t.proyecto_id = proyecto_id
    # t.fecha_creacion = fecha_creacion
    # t.desarrolladores = desarrolladores

    # #Guarda la tarea
    # t.save()
    return HttpResponseRedirect(reverse('tareas'))
