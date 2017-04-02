from rest_framework import serializers

from simulator.models.realestate import RealEstate, Flat, Room
from simulator.utils.enums import RealEstateClass


class RealEstateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = RealEstate
        fields = ('id', 'owner', 'for_rent', 'description')

    def to_representation(self, instance):
        representation = {
            'id': instance.id,
            'owner': instance.owner.id,
            'for_rent': instance.for_rent,
            'description': instance.description
        }
        if instance.real_estate_class_type == RealEstateClass.FLAT.value:
            if type(instance) is not Flat:
                instance = Flat.objects.filter(id=instance.id)[0]
            rooms = []
            for record in instance.rooms.all():
                rooms.append({
                    'id': record.id,
                    'owner': record.owner.id,
                    'for_rent': record.for_rent,
                    'description': record.description,
                    'parent_flat': record.parent_flat.id,
                    'room_type': record.room_type,
                    'square': record.square
                })
            representation.update({
                'flat_type': instance.flat_type,
                'per_room_basis': instance.per_room_basis,
                'new_build': instance.new_build,
                'rooms': rooms
            })
        elif instance.real_estate_class_type == RealEstateClass.ROOM.value:
            if type(instance) is not Room:
                instance = Room.objects.filter(id=instance.id)[0]
            representation.update({
                'parent_flat': instance.parent_flat.id,
                'room_type': instance.room_type,
                'square': instance.square
            })

        return representation

    def create(self, validated_data):
        owner_data = validated_data.pop('owner')
        realEstate = self.Meta.model.objects.create(**validated_data)
        return realEstate

    def update(self, instance, validated_data):
        super(RealEstateSerializer, self).update(self, instance, validated_data)


class FlatSerializer(RealEstateSerializer):
    rooms = serializers.HyperlinkedRelatedField(view_name='room-detail', many=True, read_only=True)

    class Meta(RealEstateSerializer.Meta):
        model = Flat
        fields = RealEstateSerializer.Meta.fields + ('flat_type', 'per_room_basis', 'new_build', 'rooms')


class RoomSerializer(RealEstateSerializer):
    class Meta(RealEstateSerializer.Meta):
        model = Room
        fields = RealEstateSerializer.Meta.fields + ('parent_flat', 'room_type', 'square')
