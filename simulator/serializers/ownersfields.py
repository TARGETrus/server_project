from rest_framework import serializers
from simulator.utils.enums import RealEstateClass


class OwnersHyperlinkField(serializers.HyperlinkedRelatedField):

    def get_url(self, obj, view_name, request, format):
        """
        Overriding this method lets us set valid view_name and queryset, depending on handled object type field.

        :param obj: RealEstate (or inheriting) model object.
        :param view_name: name of the specific RealEstate view.
        :param request: incoming request.
        :param format: url format.
        :return: modified data.
        """

        if obj.real_estate_class_type == RealEstateClass.FLAT.value:
            view_name = 'flat-detail'
        elif obj.real_estate_class_type == RealEstateClass.ROOM.value:
            view_name = 'room-detail'

        url_kwargs = {
            'pk': obj.pk
        }

        return self.reverse(view_name, kwargs=url_kwargs, request=request, format=format)
