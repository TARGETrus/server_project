from rest_framework import serializers

from simulator.models.owners import Owner
from simulator.models.realestate import RealEstate
from simulator.models.deals import Deal, Sale, Rent
from simulator.serializers.fields.ownersfields import OwnersRelatedField
from simulator.serializers.fields.realestatefields import RealEstateRelatedField


class DealSerializer(serializers.HyperlinkedModelSerializer):
    vendor = OwnersRelatedField(read_only=False, queryset=Owner.objects.all())
    customer = OwnersRelatedField(read_only=False, queryset=Owner.objects.all())
    real_estate = RealEstateRelatedField(read_only=False, queryset=RealEstate.objects.all())

    class Meta:
        model = Deal
        fields = ('url', 'id', 'vendor', 'customer', 'real_estate')


class SaleSerializer(DealSerializer):
    class Meta:
        model = Sale
        fields = DealSerializer.Meta.fields + ('deal_date',)


class RentSerializer(DealSerializer):
    class Meta:
        model = Rent
        fields = DealSerializer.Meta.fields + ('from_date', 'till_date')
