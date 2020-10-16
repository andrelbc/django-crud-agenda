import django_filters
from django_filters import filters

from .models import *


class ContatoFilter(django_filters.FilterSet):
    email = filters.CharFilter(label='Buscar por email ')
    class Meta:
        model = Contato
        fields = ['email']
