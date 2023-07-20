from django.db import models

from utils.models import Timestampable


class Producer(Timestampable, models.Model):
    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"


class Contract(Timestampable, models.Model):
    class Meta:
        verbose_name = "Контракт"
        verbose_name_plural = "Контракты"


class CreditRequest(Timestampable, models.Model):
    contract = models.ForeignKey(
        to=Contract, on_delete=models.PROTECT, related_name="credit_request"
    )

    class Meta:
        verbose_name = "Кредитная заявка"
        verbose_name_plural = "Кредитные заявки"


class Product(Timestampable, models.Model):
    producer = models.ForeignKey(
        to=Producer, on_delete=models.PROTECT, related_name="product"
    )
    credit_request = models.ForeignKey(
        to=CreditRequest, on_delete=models.PROTECT, related_name="product"
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
