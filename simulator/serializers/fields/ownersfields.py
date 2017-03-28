from rest_framework import serializers

from simulator.utils.enums import OwnerClass


class OwnersHyperlinkField(serializers.HyperlinkedRelatedField):

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
        elif obj.owner_class_type == OwnerClass.LEGAL_ENTITY.value:
            view_name = 'legalentity-detail'

        url_kwargs = {
            'pk': obj.pk
        }

        return self.reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
            'pk': view_kwargs['pk']
        }
        return self.get_queryset().get(**lookup_kwargs)

    def to_internal_value(self, data):
        """
        Terrible solution. I should find something better.

        :param data: incoming url.
        :return: see overridden method.
        """
        if 'physical-entities' in data:
            self.view_name = 'physicalentity-detail'
        elif 'legal-entities' in data:
            self.view_name = 'legalentity-detail'
        super(OwnersHyperlinkField, self).to_internal_value(data)

    def display_value(self, instance):
        return '%s: %s' % (instance.owner_class_type, instance.pk)
