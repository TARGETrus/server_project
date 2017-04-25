from itertools import chain

from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.views.generic import TemplateView

from simulator.models.deals import Deal, Sale, Rent
from simulator.utils.enums import DealClass


class AllDealsView(TemplateView):
    def get(self, request, **kwargs):

        sales = get_list_or_404(Sale)
        rents = get_list_or_404(Rent)

        context = {
            'deals': list(chain(sales, rents))
        }

        return render(request, 'deals-list.html', context)


class SingleDealView(TemplateView):
    def get(self, request, **kwargs):

        deal = get_object_or_404(Deal, pk=kwargs.get('pk'))

        if deal.deal_class_type == DealClass.SALE.value:
            deal = get_object_or_404(Sale, pk=kwargs.get('pk'))
        elif deal.deal_class_type == DealClass.RENT.value:
            deal = get_object_or_404(Rent, pk=kwargs.get('pk'))

        context = {
            'deal': deal
        }

        return render(request, 'single-deal.html', context)
