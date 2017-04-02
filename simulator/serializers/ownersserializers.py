from rest_framework import serializers

from simulator.models.owners import Owner, PhysicalEntity, LegalEntity
from simulator.serializers.realestateserializers import RealEstateSerializer
from simulator.utils.enums import OwnerClass


class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    real_estate_property = RealEstateSerializer(many=True, read_only=True)

    class Meta:
        model = Owner
        fields = ('id', 'phone_number', 'address_actual', 'address_registered', 'real_estate_property')

    def to_representation(self, instance):
        representation = super(OwnerSerializer, self).to_representation(instance)
        if instance.owner_class_type == OwnerClass.PHYSICAL_ENTITY.value:
            if type(instance) is not PhysicalEntity:
                instance = PhysicalEntity.objects.filter(id=instance.id)[0]
            representation.update({
                'first_name': instance.first_name,
                'second_name': instance.second_name,
                'third_name': instance.third_name
            })
        elif instance.owner_class_type == OwnerClass.LEGAL_ENTITY.value:
            if type(instance) is not LegalEntity:
                instance = LegalEntity.objects.filter(id=instance.id)[0]
            representation.update({
                'company_name': instance.company_name.id,
                'inn': instance.inn
            })

        return representation


class PhysicalEntitySerializer(OwnerSerializer):
    class Meta(OwnerSerializer.Meta):
        model = PhysicalEntity
        fields = OwnerSerializer.Meta.fields + ('first_name', 'second_name', 'third_name', 'gender', 'birth_date',
                                                'passport_series', 'passport_number', 'passport_issued_date')


class LegalEntitySerializer(OwnerSerializer):
    class Meta(OwnerSerializer.Meta):
        model = LegalEntity
        fields = OwnerSerializer.Meta.fields + ('company_name', 'inn')
