from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from simulator.models.orders import Order
from simulator.forms.ordersforms import OrderForm


class AllOrdersView(TemplateView):
    def get(self, request, **kwargs):

        orders = Order.objects.all()

        context = {
            'orders': orders
        }

        return render(request, 'orders-list.html', context)


def orderFormView(request):

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('flat-list')
    else:
        form = OrderForm()

    return render(request, 'orders-form.html', {'form': form})
