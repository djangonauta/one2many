from django.db import models

class Projeto(models.Model):

    nome = models.CharField(max_length=255)

    def locais_realizacao(self):
        return ', '.join(map(str, self.locais.all()))


class Local(models.Model):

    projeto = models.ForeignKey(Projeto, related_name='locais', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    numero = models.IntegerField()

    def __str__(self):
        return f'{self.nome}({self.numero})'