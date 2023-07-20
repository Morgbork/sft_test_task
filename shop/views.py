from django.http import JsonResponse
from django.views import View
from shop.models import CreditRequest


class ProducersFromCreditRequestView(View):
    def get(self, request, *args, **kwargs):
        contract_id = kwargs.get('contract_id', None)
        credit_request_data = CreditRequest.objects.filter(contract__id=contract_id).values_list('product__producer__id', flat=True)
        return JsonResponse(list(credit_request_data), safe=False)
