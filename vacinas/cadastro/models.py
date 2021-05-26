from django.db import models

class cadastroModel(models.Model):
    nome = models.CharField('Nome',max_length=50)
    idade = models.IntegerField('Idade')
    data = models.IntegerField('Data')
    numero_da_dose = models.IntegerField('Numero da Dose')

    def __str__(self):
        return self.nome

