from client.models import Client
from client.validators import *
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def validate(self, data):
        if not name_validator(data['name']):
            raise serializers.ValidationError({'name': 'Nome inválido. Deve conter apenas letras e espaços.'})
    
        if not rg_validator(data['rg']):
            raise serializers.ValidationError({'rg': 'RG inválido.'})
        
        if not cpf_validator(data['cpf']):
            raise serializers.ValidationError({'cpf': 'CPF inválido.'})
        
        if not birth_date_validator(data['birth_date']):
            raise serializers.ValidationError({'birth_date': 'Data de nascimento inválida.'})
        
        if not email_validator(data['email']):
            raise serializers.ValidationError({'email': 'E-mail inválido.'})
        
        if not phone_validator(data['phone']):
            raise serializers.ValidationError({'phone': 'Telefone inválido.'})
        
        if not status_validator(data['status']):
            raise serializers.ValidationError({'status': 'Status inválido.'})
        
        return data