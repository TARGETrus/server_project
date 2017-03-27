from django.db import models
from simulator.models.owners import Owner
from simulator.utils.enums import RealEstateType, FlatType, RoomType

REAL_ESTATE_TYPE = {
    (RealEstateType.REAL_ESTATE.value, 'RealEstate'),
    (RealEstateType.FLAT.value, 'Flat'),
    (RealEstateType.ROOM.value, 'Room')
}

FLAT_TYPE = {
    (FlatType.REGULAR.value, 'Regular'),
    (FlatType.STUDIO.value, 'Studio')
}

ROOM_TYPE = {
    (RoomType.BATHROOM.value, 'Bathroom'),
    (RoomType.KITCHEN.value, 'Kitchen'),
    (RoomType.LIVING_ROOM.value, 'Living Room')
}


class RealEstate(models.Model):
    real_estate_type = models.CharField(choices=REAL_ESTATE_TYPE, max_length=1,
                                        default=RealEstateType.REAL_ESTATE.value)
    owner = models.ForeignKey(Owner, related_name='real_estate_property', on_delete=models.PROTECT)
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
