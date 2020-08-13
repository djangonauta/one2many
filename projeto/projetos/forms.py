from django import forms
from django.core import exceptions

from . import models

class ProjetoForm(forms.ModelForm):

    class Meta:
        model = models.Projeto
        fields = ['nome']

class LocalForm(forms.ModelForm):

    def clean_numero(self):
        numero = self.cleaned_data['numero']
        if numero < 10:
            raise exceptions.ValidationError('Número menor que 10.')

        return numero

    class Meta:
        model = models.Local
        fields = ['nome', 'numero']

LocalFormSet = forms.inlineformset_factory(models.Projeto, models.Local, form=LocalForm, fields=['nome', 'numero'], extra=0)