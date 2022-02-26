from django.db import models
import uuid
from django.core.validators import RegexValidator

# Create your models here.


class Registro(models.Model):
    PAISES_CHOICES = [
        ('Argentina', 'Argentina'),
        ('Bolivia', 'Bolivia'),
        ('Brasil', 'Brasil'),
        ('Chile', 'Chile'),
        ('Colombia', 'Colombia'),
        ('Costa Rica', 'Costa Rica'),
        ('Cuba', 'Cuba'),
        ('Ecuador', 'Ecuador'),
        ('Guatemala', 'Guatemala'),
        ('Honduras', 'Honduras'),
        ('México', 'México'),
        ('Panamá', 'Panamá'),
        ('Paraguay', 'Paraguay'),
        ('Perú', 'Perú'),
        ('Uruguay', 'Uruguay'),
        ('Venezuela', 'Venezuela')
    ]
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField(max_length=200, unique=True)
    pais = models.CharField(max_length=60, choices=PAISES_CHOICES, default='Argentina')
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    telefono = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True)
    puesto_trabajo = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre}, {self.apellido}'
