from rest_framework import serializers

from simulator.models.owners import PhysicalEntity, LegalEntity
from simulator.utils.enums import OwnerClass


class RealEstateHyperlinkField(serializers.HyperlinkedRelatedField):

    def use_pk_only_optimization(self):
        """
        Default value is True, and in this case we get "rest_framework.relations.PKOnlyObject", containing only pk,
        instead of Owner model, which is not the behaviour we want.

        :return: False, to disable this behaviour.
        """
        return False

    def get_url(self, obj, view_name, request, format):
        """
        Overriding this method lets us set valid view_name and queryset, depending on handled object type field.

        :param obj: Owner (or inheriting) model object.
        :param view_name: name of the specific Owner view.
        :param request: incoming request.
        :param format: url format.
        :return: modified data.
        """

        if obj.owner_class_type == OwnerClass.PHYSICAL_ENTITY.value:
            view_name = 'physicalentity-detail'
            queryset = PhysicalEntity.objects.all()
        elif obj.owner_class_type == OwnerClass.LEGAL_ENTITY.value:
            view_name = 'legalentity-detail'
            queryset = LegalEntity.objects.all()

        url_kwargs = {
            'pk': obj.pk
        }

        return self.reverse(view_name, kwargs=url_kwargs, request=request, format=format)
