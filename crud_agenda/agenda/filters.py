import django_filters
from django.db.models import Q
from django_filters import filters

from .models import *


class ContatoFilter(django_filters.FilterSet):
    email = filters.CharFilter(label='Buscar Contato ', method='customFilter')
    class Meta:
        model = Contato
        fields = ['email']

    def customFilter(self, queryset, name, value):
        return Contato.objects.filter(Q(nome__icontains=value) | (Q(email__icontains=value)))
