from rest_framework import serializers
from simulator.models.owners import Owner, PhysicalEntity, LegalEntity


class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Owner
        fields = ('id', 'phone_number', 'address_actual', 'address_registered', 'real_estate_property')


class PhysicalEntitySerializer(OwnerSerializer):
    class Meta(OwnerSerializer.Meta):
        model = PhysicalEntity
        fields = OwnerSerializer.Meta.fields + ('first_name', 'second_name', 'third_name', 'gender', 'birth_date',
                                                'passport_series', 'passport_number', 'passport_issued_date')


class LegalEntitySerializer(OwnerSerializer):
    class Meta(OwnerSerializer.Meta):
        model = LegalEntity
        fields = OwnerSerializer.Meta.fields + ('company_name', 'inn')
