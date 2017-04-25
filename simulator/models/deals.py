from django.db import models

from simulator.models.owners import Owner
from simulator.models.realestate import RealEstate
from simulator.utils.enums import DealClass

DEAL_CLASS = {
    (DealClass.DEAL.value, 'Deal'),
    (DealClass.RENT.value, 'Rent'),
    (DealClass.SALE.value, 'Sale')
}


class Deal(models.Model):
    """
    
    """
    deal_class_type = models.CharField(choices=DEAL_CLASS, max_length=1, editable=False, default=DealClass.DEAL.value)

    vendor = models.ForeignKey(Owner, related_name='deal_vendor', on_delete=models.PROTECT)
    customer = models.ForeignKey(Owner, related_name='deal_customer', on_delete=models.PROTECT)
    real_estate = models.ForeignKey(RealEstate, related_name='deal', on_delete=models.PROTECT)


class Sale(Deal):
    deal_date = models.DateField()

    def save(self, *args, **kwargs):
        self.deal_class_type = DealClass.SALE.value
        super(Sale, self).save(*args, **kwargs)


class Rent(Deal):
    from_date = models.DateField()
    till_date = models.DateField()

    def save(self, *args, **kwargs):
        self.deal_class_type = DealClass.RENT.value
        super(Rent, self).save(*args, **kwargs)
