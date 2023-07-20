from django.contrib import admin
from shop import models


@admin.register(models.Contract)
class ContractAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CreditRequest)
class CreditRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Producer)
class ProducerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass
