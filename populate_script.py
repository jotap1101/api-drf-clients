import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

import random
from client.models import Client
from faker import Faker
from validate_docbr import CPF

def create_clients(quantity):
    fake = Faker('pt_BR')

    Faker.seed(10)
    
    for _ in range(quantity):
        name = fake.name()
        rg = "{}.{}.{}-{}".format(random.randrange(10, 99), random.randrange(100, 999), random.randrange(100, 999), random.choice([0, random.randrange(1, 9)]))
        cpf = CPF().generate(True)
        birth_date = fake.date_of_birth(minimum_age=18, maximum_age=100)
        email = '{}@{}'.format(name.lower(), fake.free_email_domain()).replace(' ', '')
        phone = "({}) {}-{}".format(random.randrange(10, 99), random.randrange(10000, 99999), random.randrange(1000, 9999))
        status = random.choice([True, False])

        client = Client(name=name, rg=rg, cpf=cpf, birth_date=birth_date, email=email, phone=phone, status=status)

        client.save()

create_clients(50)

print('Clientes criados com sucesso!')