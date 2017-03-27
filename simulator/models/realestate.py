from django.db import models
from simulator.models.owners import Owner
from simulator.utils.enums import RealEstateClass, FlatType, RoomType

REAL_ESTATE_CLASS = {
    (RealEstateClass.REAL_ESTATE.value, 'RealEstate'),
    (RealEstateClass.FLAT.value, 'Flat'),
    (RealEstateClass.ROOM.value, 'Room')
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
    real_estate_class_type = models.CharField(choices=REAL_ESTATE_CLASS, max_length=1, editable=False,
                                              default=RealEstateClass.REAL_ESTATE.value)
    owner = models.ForeignKey(Owner, related_name='real_estate_property', on_delete=models.PROTECT)
    description = models.TextField()
    for_rent = models.BooleanField(default=False)


class Flat(RealEstate):
    flat_type = models.CharField(choices=FLAT_TYPE, max_length=1)
    per_room_basis = models.BooleanField(default=False)
    new_build = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.owner_class_type = RealEstateClass.FLAT.value
        super(Flat, self).save(*args, **kwargs)


class Room(RealEstate):
    parent_flat = models.ForeignKey(Flat, on_delete=models.PROTECT)
    room_type = models.CharField(choices=ROOM_TYPE, max_length=1)
    square = models.SmallIntegerField()

    def save(self, *args, **kwargs):
        self.owner_class_type = RealEstateClass.ROOM.value
        super(Room, self).save(*args, **kwargs)
