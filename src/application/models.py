import uuid
from django.db import models


class DateCreatedModelMixin(models.Model):
    id = models.BigAutoField(
        primary_key=True,
        unique=True,
    )

    date_created = models.DateField(auto_now_add=True)
    class Meta:
        abstract = True


class Producer(DateCreatedModelMixin):
    pass


class Application(DateCreatedModelMixin):
    pass


class Product(DateCreatedModelMixin):
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
    )

    name = models.CharField(
        max_length=255,
        unique=False,
        null=False,
    )

    producer = models.ForeignKey(
        Producer,
        on_delete=models.CASCADE,
        related_name="products",
    )
    application = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        related_name="products",
    )



class Contract(DateCreatedModelMixin):
    application = models.OneToOneField(
        Application,
        on_delete=models.CASCADE,
        related_name="contract",
    )