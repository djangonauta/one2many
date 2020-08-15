from django.db import models

def caminho_projeto(instance, filename):
    return f'projetos/{instance.nome}/{filename}'

class Projeto(models.Model):

    nome = models.CharField(max_length=255)
    arquivo = models.FileField(upload_to=caminho_projeto)

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