from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(blank = True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  
    def __str__(self):
        return self.titulo
      
    class Meta:
          db_table = 'evento'
          
    def get_data_evento(self):
        return self.data_evento.strftime(' no dia %d/%m/%Y às %H:%m hrs.')
        
    def get_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')
      
