from rest_framework import serializers
from simulator.models.realestate import RealEstate, Flat, Room
from simulator.models.owners import Owner
from simulator.serializers.realestatefields import RealEstateHyperlinkField


class RealEstateSerializer(serializers.HyperlinkedModelSerializer):
    owner = RealEstateHyperlinkField(view_name='owner-detail', queryset=Owner.objects.all())

    class Meta:
        model = RealEstate
        fields = ('url', 'id', 'owner', 'for_rent')


class FlatSerializer(RealEstateSerializer):
    class Meta(RealEstateSerializer.Meta):
        model = Flat
        fields = RealEstateSerializer.Meta.fields + ('description', 'flat_type', 'per_room_basis', 'new_build')


class RoomSerializer(RealEstateSerializer):
    class Meta(RealEstateSerializer.Meta):
        model = Room
        fields = RealEstateSerializer.Meta.fields + ('parent_flat', 'room_type', 'square')
