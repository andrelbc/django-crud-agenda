from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{8,15}$',
                                 message="Número precissa estar no formato: '+999999999'. Até 15 digitos permitidos.")
    phone_number = models.CharField(validators=[phone_regex], max_length=16, blank=True)  # validators should be a list
