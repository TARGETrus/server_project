from rest_framework import serializers
from simulator.models.owners import Owner, PhysicalEntity, LegalEntity
from simulator.serializers.ownersfields import OwnersHyperlinkField


class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    real_estate_property = OwnersHyperlinkField(view_name='realestate-detail', many=True, read_only=True)

    class Meta:
        model = Owner
        fields = ('url', 'id', 'phone_number', 'address_actual', 'address_registered', 'real_estate_property')


class PhysicalEntitySerializer(OwnerSerializer):
    class Meta(OwnerSerializer.Meta):
        model = PhysicalEntity
        fields = OwnerSerializer.Meta.fields + ('first_name', 'second_name', 'third_name', 'gender', 'birth_date',
                                                'passport_series', 'passport_number', 'passport_issued_date')


class LegalEntitySerializer(OwnerSerializer):
    class Meta(OwnerSerializer.Meta):
        model = LegalEntity
        fields = OwnerSerializer.Meta.fields + ('company_name', 'inn')
