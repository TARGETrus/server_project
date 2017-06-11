from django.forms import ModelForm

from simulator.models.orders import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['client_name', 'phone_number', 'description']
        labels = {
            'client_name': 'Ваше имя:',
            'phone_number': 'Номер телефона:',
            'description': 'Текст обращения:',
        }
