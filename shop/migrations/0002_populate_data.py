from django.db import migrations


def populate_data(apps, schema_editor):
    Producer = apps.get_model("shop", "Producer")
    Contract = apps.get_model("shop", "Contract")
    CreditRequest = apps.get_model("shop", "CreditRequest")
    Product = apps.get_model("shop", "Product")

    producer_1 = Producer.objects.create()
    producer_2 = Producer.objects.create()
    producer_3 = Producer.objects.create()

    contract_1 = Contract.objects.create()
    contract_2 = Contract.objects.create()

    credit_request_1 = CreditRequest.objects.create(contract=contract_1)
    credit_request_2 = CreditRequest.objects.create(contract=contract_2)

    products = [
        {"producer": producer_1, "credit_request": credit_request_1},
        {"producer": producer_2, "credit_request": credit_request_1},
        {"producer": producer_1, "credit_request": credit_request_2},
        {"producer": producer_2, "credit_request": credit_request_2},
        {"producer": producer_3, "credit_request": credit_request_1},
    ]

    for product in products:
        Product.objects.create(**product)


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(populate_data),
    ]
