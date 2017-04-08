from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist

from simulator.utils.structures import HashDict


class OwnersRelatedField(serializers.RelatedField):

    default_error_messages = {
        'does_not_exist': 'Invalid pk "{pk_value}" - object does not exist.',
        'incorrect_type': 'Incorrect type, received {data_type}.'
    }

    def to_internal_value(self, incoming):
        """
        Queryset with the instance we will store.

        :param incoming: instance with incoming data.
        :return: queryset.
        """
        try:
            return self.get_queryset().get(pk=incoming)
        except ObjectDoesNotExist:
            self.fail('does_not_exist', pk_value=incoming)
        except (TypeError, ValueError):
            self.fail('incorrect_type', data_type=type(incoming).__name__)

    def to_representation(self, outgoing):
        """
        Custom HashDict() is used to satisfy django and get dict on view instead of simple String.

        :param outgoing: instance we will take data from.
        :return: instance we will send with outgoing's data.
        """
        result = HashDict()
        result['id'] = outgoing.pk
        result['object_type'] = outgoing.owner_class_type

        return result

    def display_value(self, instance):
        """
        Defines what choices user will see on view's form select element.

        :param instance: instance object with data
        :return: string with select's choice.
        """
        return 'OwnerID: %s' % instance.id
