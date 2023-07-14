""" This script resolve test task."""

import os
import time
import functools
import django
from django.db import connection, reset_queries


os.environ['DJANGO_SETTINGS_MODULE'] = 'sft.settings'
django.setup()


from application.models import Producer
from test_data import insert_data


def query_debugger(func):

    @functools.wraps(func)
    def inner_func(*args, **kwargs):

        reset_queries()
        
        start_queries = len(connection.queries)

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        end_queries = len(connection.queries)
        for q in connection.queries:
            print('\n\n', q)

        print(f"Function : {func.__name__}")
        print(f"Number of Queries : {end_queries - start_queries}")
        print(f"Finished in : {(end - start):.2f}s")
        return result

    return inner_func


@query_debugger
def get_unique_producers_id(contract_id: int):

    producers = Producer.objects.filter(
        products__application__contract=contract_id,
    ).distinct(
        "id",
    ).values('id')

    # this print was added in order to view queries in the database
    for p in producers:
        print(p["id"])
    return producers


@query_debugger
def get_unique_producers_models(contract_id: int):
    producers = Producer.objects.prefetch_related(
        'products',
    ).filter(
        products__application__contract=contract_id,
    ).distinct(
        "id",
    )

    # this print was added in order to view queries in the database
    for pr in producers:
        print(pr.products.all())
    return producers


if __name__ == "__main__":
    insert_data()
    get_unique_producers_id(23)
    get_unique_producers_models(23)
