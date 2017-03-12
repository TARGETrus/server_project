from django.db import models
from .owners import Owner
from .flats import Flat

ROOM_TYPE = (
    ('B', 'Bathroom'),
    ('K', 'Kitchen'),
    ('L', 'Living Room')
)


class Room(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.PROTECT)
    flat = models.ForeignKey(Flat, on_delete=models.PROTECT)
    square = models.SmallIntegerField()
    price = models.IntegerField()
    rent_price = models.IntegerField()
    # etc
    type = models.CharField()
