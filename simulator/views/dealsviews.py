from itertools import chain

from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.views.generic import TemplateView

from simulator.models.deals import Deal, Sale, Rent
from simulator.utils.genericgetters import GenericGetters


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

        deal = GenericGetters.get_specific_deal(get_object_or_404(Deal, pk=kwargs.get('pk')))
        vendor = GenericGetters.get_specific_owner(deal.vendor)
        customer = GenericGetters.get_specific_owner(deal.customer)
        real_estate = GenericGetters.get_specific_restate(deal.real_estate)

        context = {
            'deal': deal,
            'vendor': vendor,
            'customer': customer,
            'real_estate': real_estate
        }

        return render(request, 'single-deal.html', context)


