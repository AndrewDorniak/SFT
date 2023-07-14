from random import randint

from django.db import transaction

from application.models import (
    Producer,
    Product,
    Contract,
    Application,
)


def insert_data():
    produsers = [Producer() for _ in range(10)]
    applications = [Application() for _ in range(20)]
    contracts = [Contract(application=i) for i in applications]
    products = [
        Product(
            name=f'Product{i}',
            producer=produsers[randint(0, 9)],
            application=applications[randint(0, 19)]
        ) for i in range(1, 100)
    ]

    with transaction.atomic():
        Producer.objects.bulk_create(produsers)
        Application.objects.bulk_create(applications)
        Contract.objects.bulk_create(contracts)
        Product.objects.bulk_create(products)
