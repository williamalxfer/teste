from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User



class Produto(models.Model):
   CATEGORIA_CHOICES = (
      ('Aperitivos', 'Aperitivos'),
      ('Bebidas', 'Bebidas'),
      ('Biscoitos', 'Biscoitos'),
      ('Carnes', 'Carnes'),
      ('Massas', 'Massas'),
   )
   UNIDADE_CHOICES = (
      ('UN', 'UN'),
      ('PC', 'PC'),
      ('KG', 'KG'),
      ('LT', 'LT'),
      ('PÇ', 'PÇ'),
   )
   nome = models.CharField(max_length=100)  
   marca = models.CharField(default='', max_length=100)
   descricao = models.TextField()
   unidade = models.CharField(max_length=2, choices = UNIDADE_CHOICES) # KG, LT, PÇ
   valor = models.FloatField(default=0.0) 
   categoria = models.CharField(max_length=100, choices = CATEGORIA_CHOICES)
   quantidade = models.IntegerField(default=0)
   foto = models.FileField(upload_to="%Y/%m/%d/", blank=True)
   data_cadastro = models.DateTimeField(default=timezone.now) 
   curtidas = models.IntegerField(default=0)   
   descurtidas = models.IntegerField(default=0)
   visualizacoes = models.IntegerField(default=0)
   
   def __str__(self):
      return self.nome + " - R$ " + str(self.valor)  +  "  || DESCRIÇÃO: " + str(self.descricao) + "  || CATEGORIA: " + str(self.categoria) + " || ESTOQUE:" + " (" + str(self.quantidade) + ") ||"           
  
 
 
class Mensagem(models.Model):

   nome = models.CharField(max_length=100)
   email = models.EmailField(max_length=200)
   assunto = models.CharField(max_length=100)
   texto = models.TextField()
   data = models.DateTimeField(default=timezone.now)

   def __str__(self):
      return self.nome + ': ' + self.assunto