from django.db import models
from .owners import Owner

FLAT_TYPE = (
    ('R', 'Regular'),
    ('S', 'Studio')
)

ROOM_TYPE = (
    ('B', 'Bathroom'),
    ('K', 'Kitchen'),
    ('L', 'Living Room')
)


class RealEstate(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.PROTECT)
    for_rent = models.BooleanField(default=False)


class Flat(RealEstate):
    description = models.TextField()
    flat_type = models.CharField(choices=FLAT_TYPE, max_length=1)
    per_room_basis = models.BooleanField(default=False)
    new_build = models.BooleanField(default=False)


class Room(RealEstate):
    parent_flat = models.ForeignKey(Flat, on_delete=models.PROTECT)
    room_type = models.CharField(choices=ROOM_TYPE, max_length=1)
    square = models.SmallIntegerField()
