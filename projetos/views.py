from django import shortcuts
from django.contrib import messages

from . import forms, models


def criar(request):
    if request.method == 'GET':
        projeto_form = forms.ProjetoForm()
        locais_inline_form = forms.LocalFormSet()
        return shortcuts.render(request, 'projetos.html', {
            'projeto_form': projeto_form,
            'locais_inline_form': locais_inline_form,
            'projetos': models.Projeto.objects.all(),
        })

    projeto_form = forms.ProjetoForm(request.POST, request.FILES)
    locais_inline_form = forms.LocalFormSet(request.POST, request.FILES)
    if projeto_form.is_valid() and locais_inline_form.is_valid():
        projeto = projeto_form.save()
        locais_inline_form.instance = projeto
        locais_inline_form.save()
        messages.success(request, 'Projeto criado com sucesso')
        return shortcuts.redirect('/')

    return shortcuts.render(request, 'projetos.html', {
        'projeto_form': projeto_form,
        'locais_inline_form': locais_inline_form,
        'projetos': models.Projeto.objects.all(),
    })


def editar(request, pk=None):
    projeto = shortcuts.get_object_or_404(models.Projeto, pk=pk)
    if request.method == 'GET':
        projeto_form = forms.ProjetoForm(instance=projeto)
        locais_inline_form = forms.LocalFormSet(instance=projeto)
        return shortcuts.render(request, 'projetos.html', {
            'projeto_form': projeto_form,
            'locais_inline_form': locais_inline_form,
            'projetos': models.Projeto.objects.all(),
        })

    projeto_form = forms.ProjetoForm(request.POST, request.FILES, instance=projeto)
    locais_inline_form = forms.LocalFormSet(request.POST, request.FILES, instance=projeto)
    if projeto_form.is_valid() and locais_inline_form.is_valid():
        projeto_form.save()
        locais_inline_form.save()
        messages.info(request, 'Projeto Atualizado com sucesso')
        return shortcuts.redirect('/')

    return shortcuts.render(request, 'projetos.html', {
        'projeto_form': projeto_form,
        'locais_inline_form': locais_inline_form,
        'projetos': models.Projeto.objects.all(),
    })


def remover(request, pk=None):
    projeto = shortcuts.get_object_or_404(models.Projeto, pk=pk)
    if request.method == 'GET':
        return shortcuts.render(request, 'remover_projeto.html', {
            'projeto': projeto
        })

    projeto.delete()
    messages.warning(request, 'Projeto removido com sucesso')
    return shortcuts.redirect('/')