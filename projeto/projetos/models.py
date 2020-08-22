from django.db import models


class TagChoices(models.IntegerChoices):

    CADASTRO_ANDAMENTO = 1, 'Cadastro em Andamento'
    AGUARDANDO_APROVACAO = 2, 'Aguardando Aprovação'
    APROVADO = 3, 'Aprovado'
    REPROVADO = 4, 'Reprovado'
    REMOVIDO = 5, 'Removido'


class Tag(models.Model):

    id = models.IntegerField(primary_key=True, choices=TagChoices.choices)

    def __str__(self):
        return self.get_id_display()


def caminho_projeto(instance, filename):
    return f'projetos/{instance.nome}/{filename}'

class Projeto(models.Model):

    nome = models.CharField(max_length=255)
    arquivo = models.FileField(upload_to=caminho_projeto)
    tags = models.ManyToManyField(Tag, related_name='projetos')

    def locais_realizacao(self):
        return ', '.join(map(str, self.locais.all()))


def caminho_local(instance, filename):
    return f'projetos/{instance.projeto.nome}/{instance.id}/{filename}'

class Local(models.Model):

    projeto = models.ForeignKey(Projeto, related_name='locais', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    numero = models.IntegerField()
    arquivo = models.FileField(upload_to=caminho_local)

    def __str__(self):
        return f'{self.nome}({self.numero})'