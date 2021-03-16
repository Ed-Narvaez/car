# coding:utf-8

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.mail import EmailMessage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ComentarioForm, ContactoForm, AutoForm, TipoForm, MarcaForm
from .models import Comentario, Auto, Marca, Tipo


@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')

def comentario_nuevo(request):
    if request.method=='POST':
        formulario = ComentarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/autos')
    else:
        formulario = ComentarioForm()
    context = {'formulario': formulario}
    return render(request, 'autos_comentarioform.html', context)

def contacto(request):
    if request.method=='POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            titulo = 'Mensaje desde el mobiliario de Maestros del Web'
            contenido = formulario.cleaned_data['mensaje'] + "\n"
            contenido += 'Comunicarse a: ' + formulario.cleaned_data['correo']
            correo = EmailMessage(titulo, contenido, to=['destinatario@email.com'])
            try:
                correo.send()
            except Exception as e:
                print('No fue posible enviar el mensaje, revisar la configuración')
                print(e)
            return HttpResponseRedirect('/')
    else:
        formulario = ContactoForm()
    context = {'formulario': formulario}
    return render(request, 'recetas_contactoform.html',context)

def inicio(request):
    autos = Auto.objects.all()
    context = {'autos': autos}
    return render(request, 'autos_inicio.html', context)

def ingresar(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/privado')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/privado')
                else:
                    return render(request, 'noactivo.html')
            else:
                return render(request, 'nousuario.html')
    else:
        formulario = AuthenticationForm()
    context = {'formulario': formulario}
    return render(request, 'ingresar.html', context)

@login_required(login_url='/ingresar')
def privado(request):
    usuario = request.user
    context = {'usuario': usuario}
    return render(request, 'privado.html', context)

def auto(request, id_auto):
    dato = get_object_or_404(Auto, pk=id_auto)
    comentarios = Comentario.objects.filter(auto=dato)
    context = {'auto': dato, 'comentarios': comentarios}
    return render(request, 'autos_auto.html', context)

def auto_nuevo(request):
    if request.method=='POST':
        formulario = AutoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/autos')
    else:
        formulario = RecetaForm()
    context = {'formulario': formulario}
    return render(request, 'autos_autoform.html', context)


def autos(request):
    autos = Auto.objects.all()
    context = {'datos': autos}
    return render(request, 'autos_lista_autos.html', context)

def usuarios(request):
    usuarios = User.objects.all()
    autos = Auto.objects.all()
    context = {'autos': autos, 'usuarios':usuarios}
    return render(request, 'autos_usuarios.html', context)

def usuario_nuevo(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    context = {'formulario': formulario}
    return render(request, 'nuevousuario.html', context)

def sobre(request):
    html = "<html><body>Proyecto de autos</body></html>"
    return HttpResponse(html)
