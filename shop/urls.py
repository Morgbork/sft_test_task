from django.urls import path

from shop.views import ProducersFromCreditRequestView

urlpatterns = [
    path(
        "contracts/<int:contract_id>/producers/",
        ProducersFromCreditRequestView.as_view(),
        name="producers-ids",
    ),
]
