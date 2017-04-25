from django.db import models


class PricesManager(models.Manager):
    def get_latest_price(self):
        return super(PricesManager, self).get_queryset().order_by('established_date')[0]
