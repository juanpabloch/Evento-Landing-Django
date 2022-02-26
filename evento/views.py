from django.shortcuts import render, redirect
from evento.forms import RegistroForm, UserRegistro
from evento.models import Registro
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
import environ

import smtplib, ssl
# Create your views here.

env = environ.Env(DEBUG=(bool, False))

PORT = 465
CONTEXT = ssl.create_default_context()
my_email = "webinarcxfinanciero@gmail.com"
my_password = env("EMAIL_PASSWORD")

def send_email(email, name):
    frase = """
    !!! Gracias por registrate !!!
    En este webinar trataremos la temática de cómo humanizar la experiencia del cliente de 
    Banca y Seguros en el nuevo entorno digital.
    ¡Te esperamos!
    """
    message = f"Subject: Gracias {name} por registrarte!\n\n {frase}"
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", port=PORT, context=CONTEXT) as server:
            server.login(user=my_email, password=my_password)
            server.sendmail(from_addr=my_email, to_addrs=email, msg=message.encode('utf-8'))
    except:
        print("error al enviar")
    print("email enviado")


def index(request):
    form = RegistroForm()
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            send_email(form_data['email'], form_data['nombre'])
            form.save()
            form = RegistroForm()
            context = {
                'form': form,
                'active': 'active'
            }
            return render(request, 'evento/index.html', context)
    context = {
        'form': form,
        'active': ''
    }
    return render(request, 'evento/index.html', context)


@login_required(login_url='login')
def lista_personas(request):
    lista = Registro.objects.all()
    context = {
        'lista': lista
    }
    return render(request, 'evento/lista.html', context)


def login_user(request):
    form = UserRegistro()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('listado')
        else:
            messages.error(request, 'usuario o password incorrectos')
    context = {
        'form': form
    }
    return render(request, 'evento/login.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


def registro_acceso_lista(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    key = request.GET.get('key')
    if key != env("REGISTRATION_KEY"):
        messages.error(request, 'la clave es invalida')
        return redirect('login')
    try:
        User.objects.create_user(username=username, password=password)
    except:
        messages.error(request, 'Error inesperado vuelva a intentar')
        return redirect('login')

    messages.success(request, 'Creado exitosamente')
    return redirect('login')

