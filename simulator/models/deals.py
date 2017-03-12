from django.db import models
from .owners import Owner


class Deal(models.Model):
    vendor = models.ForeignKey(Owner, on_delete=models.PROTECT)
    customer = models.ForeignKey(Owner, on_delete=models.PROTECT)
    price = models.PositiveIntegerField()


class Sale(Deal):
    deal_date = models.DateField()


class Rent(Deal):
    from_date = models.DateField()
    till_date = models.DateField()
