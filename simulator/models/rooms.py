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
    room_type = models.CharField(choices=ROOM_TYPE, max_length=1)
    square = models.SmallIntegerField()
    price = models.IntegerField()
    rent_price = models.IntegerField()
    # etc
    for_rent = models.BooleanField(default=False)
