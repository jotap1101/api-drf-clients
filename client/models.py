from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    rg = models.CharField(max_length=255, verbose_name='RG', unique=True)
    cpf = models.CharField(max_length=255, verbose_name='CPF', unique=True)
    birth_date = models.DateField(verbose_name='Data de Nascimento')
    email = models.EmailField(max_length=255, verbose_name='E-mail')
    phone = models.CharField(max_length=255, verbose_name='Telefone')
    status = models.BooleanField(default=True, verbose_name='Status')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.name