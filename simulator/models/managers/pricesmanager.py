from django.db import models

from simulator.utils.enums import PriceType


class PricesManager(models.Manager):
    def get_sell_prices(self, pk):
        return super(PricesManager, self).get_queryset().filter(
            price_type=PriceType.SALE.value, real_estate_id=pk).order_by('established_date')

    def get_rent_prices(self, pk):
        return super(PricesManager, self).get_queryset().filter(
            price_type=PriceType.RENT.value, real_estate_id=pk).order_by('established_date')
