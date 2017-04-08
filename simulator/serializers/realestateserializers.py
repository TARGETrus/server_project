from rest_framework import serializers

from simulator.models.owners import Owner
from simulator.models.realestate import RealEstate, Flat, Room
from simulator.serializers.fields.ownersfields import OwnersRelatedField


class RealEstateSerializer(serializers.HyperlinkedModelSerializer):
    owner = OwnersRelatedField(read_only=False, queryset=Owner.objects.all())

    class Meta:
        model = RealEstate
        fields = ('url', 'id', 'owner', 'for_rent')


class FlatSerializer(RealEstateSerializer):
    rooms = serializers.HyperlinkedRelatedField(view_name='room-detail', many=True, read_only=True)

    class Meta(RealEstateSerializer.Meta):
        model = Flat
        fields = RealEstateSerializer.Meta.fields + ('description', 'floor', 'flat_type', 'per_room_basis', 'new_build',
                                                     'rooms')


class RoomSerializer(RealEstateSerializer):
    class Meta(RealEstateSerializer.Meta):
        model = Room
        fields = RealEstateSerializer.Meta.fields + ('parent_flat', 'room_type', 'square')
