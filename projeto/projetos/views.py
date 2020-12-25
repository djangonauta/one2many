from django import shortcuts
from django.contrib import messages

from . import forms, models


def criar(request):
    if request.method == 'GET':
        form = forms.ProjetoForm()
        inline_form = forms.LocalFormSet()
        return shortcuts.render(request, 'projetos.html', {
            'form': form,
            'inline_form': inline_form,
            'projetos': models.Projeto.objects.all(),
        })

    form = forms.ProjetoForm(request.POST, request.FILES)
    inline_form = forms.LocalFormSet(request.POST, request.FILES)
    if form.is_valid() and inline_form.is_valid():
        projeto = form.save()
        inline_form.instance = projeto
        inline_form.save()
        messages.success(request, 'Projeto criado com sucesso')
        return shortcuts.redirect('/')

    return shortcuts.render(request, 'projetos.html', {
        'form': form,
        'inline_form': inline_form,
        'projetos': models.Projeto.objects.all(),
    })


def editar(request, pk=None):
    projeto = shortcuts.get_object_or_404(models.Projeto, pk=pk)
    if request.method == 'GET':
        form = forms.ProjetoForm(instance=projeto)
        inline_form = forms.LocalFormSet(instance=projeto)
        return shortcuts.render(request, 'projetos.html', {
            'form': form,
            'inline_form': inline_form,
            'projetos': models.Projeto.objects.all(),
        })

    form = forms.ProjetoForm(request.POST, request.FILES, instance=projeto)
    inline_form = forms.LocalFormSet(request.POST, request.FILES, instance=projeto)
    if form.is_valid() and inline_form.is_valid():
        form.save()
        inline_form.save()
        messages.info(request, 'Projeto Atualizado com sucesso')
        return shortcuts.redirect('/')

    return shortcuts.render(request, 'projetos.html', {
        'form': form,
        'inline_form': inline_form,
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
