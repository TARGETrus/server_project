from django.db import models
from .realestate import RealEstate

PRICE_TYPE = (
    ('R', 'Rent'),
    ('S', 'Sale')
)


class Price(models.Model):
    real_estate = models.ForeignKey(RealEstate, on_delete=models.PROTECT)
    price = models.PositiveIntegerField(null=True)
    price_type = models.CharField(choices=PRICE_TYPE, max_length=1)
    established_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('established_date',)
