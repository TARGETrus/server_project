from django.db import models
from .owners import Owner

FLAT_TYPE = (
    ('R', 'Regular'),
    ('S', 'Studio')
)


class Flat(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.PROTECT)
    flat_type = models.CharField(choices=FLAT_TYPE, max_length=1)
    description = models.TextField()
    for_rent = models.BooleanField(default=False)
    new_build = models.BooleanField(default=False)
