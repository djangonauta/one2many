from django import shortcuts
from django.views import generic
from django.contrib import messages

from . import forms, models

def criar(request):
    if request.method ==  'GET':
        form = forms.ProjetoForm()
        inline_form = forms.LocalFormSet()
        return shortcuts.render(request, 'projetos.html', {
            'form': form,
            'inline_form': inline_form,
            'projetos': models.Projeto.objects.all(),
            'atualizar': False,
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
        'atualizar': False,
    })

def editar(request, pk=None):
    projeto = shortcuts.get_object_or_404(models.Projeto, pk=pk)
    if request.method ==  'GET':
        form = forms.ProjetoForm(instance=projeto)
        inline_form = forms.LocalFormSet(instance=projeto)
        return shortcuts.render(request, 'projetos.html', {
            'form': form,
            'inline_form': inline_form,
            'projetos': models.Projeto.objects.all(),
            'atualizar': True,
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
        'atualizar': True,
    })

def remover(request, pk=None):
    projeto = shortcuts.get_object_or_404(models.Projeto, pk=pk)
    if request.method == 'GET':
        return shortcuts.render(request, '', {
            'projeto': projeto
        })

    projeto.delete()
    return shortcuts.redirect('/')


class RemoverProjetoView(generic.DeleteView):

    template_name = 'remover_projeto.html'
    model = models.Projeto
    success_url = '/'
    
    def delete(self, request, *args, **kwargs):
        messages.warning(request, 'Projeto removido com sucesso')
        return super().delete(request, *args, **kwargs)


remover = RemoverProjetoView.as_view()
