from django.shortcuts import render
from django.views.generic import TemplateView


from simulator.models.orders import Order


class AllOrdersView(TemplateView):
    def get(self, request, **kwargs):

        orders = Order.objects.all()

        context = {
            'orders': orders
        }

        return render(request, 'orders-list.html', context)
