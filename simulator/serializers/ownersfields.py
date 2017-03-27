from rest_framework import serializers
from simulator.utils.enums import RealEstateClass


class OwnersHyperlinkField(serializers.HyperlinkedRelatedField):

    def get_url(self, obj, view_name, request, format):

        if obj.real_estate_class_type == RealEstateClass.FLAT.value:
            view_name = 'flat-detail'
        elif obj.real_estate_class_type == RealEstateClass.ROOM.value:
            view_name = 'room-detail'

        url_kwargs = {
            'pk': obj.pk
        }

        print(obj.real_estate_class_type)

        return self.reverse(view_name, kwargs=url_kwargs, request=request, format=format)
