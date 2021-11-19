from django.shortcuts import render
from django.views.generic import ListView
from bitcoinBTC.models import Currency


class CurrencyView(ListView):

    def get(self, request):
        currency_list = Currency.objects.all()
        return render(request, "base.html", {"usersCurrency_list": currency_list})
