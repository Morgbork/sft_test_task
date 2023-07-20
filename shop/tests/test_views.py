import pytest
from django.urls import reverse
from shop.models import CreditRequest, Producer, Product, Contract


@pytest.mark.django_db
def test_producers_from_credit_request_view(client):
    producer_1 = Producer.objects.create()
    producer_2 = Producer.objects.create()
    producer_3 = Producer.objects.create()

    contract_1 = Contract.objects.create()
    contract_2 = Contract.objects.create()

    credit_request_1 = CreditRequest.objects.create(contract=contract_1)
    credit_request_2 = CreditRequest.objects.create(contract=contract_2)

    products = [
        {'producer': producer_1, 'credit_request': credit_request_1},
        {'producer': producer_2, 'credit_request': credit_request_1},
        {'producer': producer_1, 'credit_request': credit_request_2},
        {'producer': producer_2, 'credit_request': credit_request_2},
        {'producer': producer_3, 'credit_request': credit_request_1},
    ]

    for product in products:
        Product.objects.create(**product)

    url = reverse('producers-ids', args=[credit_request_1.id])
    response = client.get(url)

    assert response.status_code == 200

    expected_data = [producer_1.id, producer_2.id, producer_3.id]
    assert response.json() == expected_data

    # Test not existing credit request;
    url = reverse('producers-ids', args=[0])
    response = client.get(url)

    assert response.status_code == 200

    expected_data = []
    assert response.json() == expected_data
