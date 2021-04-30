from django import forms
from django.core import exceptions

from . import models


class ProjetoForm(forms.ModelForm):

    class Meta:
        model = models.Projeto
        fields = ['nome', 'arquivo', 'tags']

    def atualizar(self):
        return self.instance.pk is not None


class LocalForm(forms.ModelForm):

    class Meta:
        model = models.Local
        fields = ['nome', 'numero', 'arquivo']

    def clean_numero(self):
        numero = self.cleaned_data['numero']
        if numero < 10:
            raise exceptions.ValidationError('Número menor que 10.')

        return numero


class ApelidoForm(forms.ModelForm):

    class Meta:
        model = models.Apelido
        fields = ['nome']


LocalFormSet = forms.inlineformset_factory(
    models.Projeto,
    models.Local,
    form=LocalForm,
    fields=['nome', 'numero', 'arquivo'],
    extra=0,
)


ApelidoFormSet = forms.inlineformset_factory(
    models.Projeto,
    models.Apelido,
    form=ApelidoForm,
    fields=ApelidoForm.Meta.fields,
    extra=0,
)
