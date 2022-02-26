from django.shortcuts import render, redirect
from evento.forms import RegistroForm, UserRegistro
from evento.models import Registro
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

import smtplib, ssl
# Create your views here.

PORT = 465
CONTEXT = ssl.create_default_context()
my_email = "webinarcxfinanciero@gmail.com"
my_password = 'asd567jkl123'

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
