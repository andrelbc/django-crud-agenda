from django import forms
from .models import Contato


class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'
        labels = {
            'nome': 'Nome Completo',
            'phone_number': 'Telefone',
        }

    def __init__(self, *args, **kwargs):
        super(FormContato, self).__init__(*args, **kwargs)
        self.fields['email'].unique = True
