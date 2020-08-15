from django import shortcuts

from . import forms, models

def index(request):
    if request.method ==  'GET':
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
        return shortcuts.redirect('/')

    return shortcuts.render(request, 'projetos.html', {
        'form': form,
        'inline_form': inline_form,
        'projetos': models.Projeto.objects.all(),
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
        })

    form = forms.ProjetoForm(request.POST, request.FILES, instance=projeto)
    inline_form = forms.LocalFormSet(request.POST, request.FILES, instance=projeto)
    if form.is_valid() and inline_form.is_valid():
        form.save()
        inline_form.save()
        return shortcuts.redirect('/')

    return shortcuts.render(request, 'projetos.html', {
        'form': form,
        'inline_form': inline_form,
        'projetos': models.Projeto.objects.all(),
    })

def remover(request, pk=None):
    projeto = shortcuts.get_object_or_404(models.Projeto, pk=pk)
    projeto.delete()
    return shortcuts.redirect('/')