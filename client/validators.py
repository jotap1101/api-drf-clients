import re
from validate_docbr import CPF

def name_validator(value):
    return re.match(r'^[a-zA-ZçÇ\s]+$', value) # A-Z, a-z, ç, Ç, espaço

def rg_validator(value):
    return re.match(r'^\d{2}\.\d{3}\.\d{3}-\d$|^\d{2}\.\d{3}\.\d{3}$|^\d{8}$|^\d{9}$', value) # 00.000.000-0, 00.000.000, 00000000, 000000000

def cpf_validator(value):
    # return re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$|^\d{11}$', value) # 000.000.000-00, 00000000000
    cpf = CPF()

    return cpf.validate(value) # CPF válido (utilizando a biblioteca validate_docbr)

def birth_date_validator(value):
    return value.year >= 1900 # Data de nascimento deve ser maior ou igual a 1900

def email_validator(value):
    return re.match(r'^.+@.+\..+$', value) # Qualquer caractere seguido de @ seguido de qualquer caractere seguido de .

def phone_validator(value):   
    return re.match(r'^\(\d{2}\) \d{5}-\d{4}$|^\d{2} \d{5}-\d{4}$|^\d{11}$', value) # (00) 00000-0000, 00 00000-0000, 00000000000

def status_validator(value):
    return isinstance(value, bool) # Deve ser um booleano