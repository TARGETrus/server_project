from django.db import models
from simulator.models.realestate import RealEstate
from simulator.utils.enums import PriceType

PRICE_TYPE = (
    (PriceType.RENT.value, 'Rent'),
    (PriceType.SALE.value, 'Sale')
)


class Price(models.Model):
    real_estate = models.ForeignKey(RealEstate, on_delete=models.PROTECT)
    price = models.PositiveIntegerField(null=True)
    price_type = models.CharField(choices=PRICE_TYPE, max_length=1)
    established_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('established_date',)
