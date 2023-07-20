from django.urls import path
from shop.views import ProducersFromCreditRequestView

urlpatterns = [
    path('producers-ids/<int:contract_id>/', ProducersFromCreditRequestView.as_view(), name='producers-ids'),
]
