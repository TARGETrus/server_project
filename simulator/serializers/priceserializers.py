from rest_framework import serializers

from simulator.models.realestate import RealEstate
from simulator.models.prices import Price
from simulator.serializers.fields.realestatefields import RealEstateRelatedField


class PriceSerializer(serializers.HyperlinkedModelSerializer):
    real_estate = RealEstateRelatedField(read_only=False, queryset=RealEstate.objects.all())

    class Meta:
        model = Price
        fields = ('url', 'id', 'price', 'price_type', 'established_date', 'real_estate')
