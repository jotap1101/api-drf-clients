# Generated by Django 5.0.4 on 2024-05-05 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_alter_client_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='cpf',
            field=models.CharField(max_length=255, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='client',
            name='rg',
            field=models.CharField(max_length=255, unique=True, verbose_name='RG'),
        ),
    ]
