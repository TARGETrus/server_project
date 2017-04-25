from itertools import chain

from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.views.generic import TemplateView

from simulator.models.owners import Owner, PhysicalEntity, LegalEntity
from simulator.models.realestate import Flat, Room
from simulator.utils.enums import RealEstateClass
from simulator.utils.genericgetters import GenericGetters


class AllOwnersView(TemplateView):
    def get(self, request, **kwargs):

        physical_entities = get_list_or_404(PhysicalEntity)
        legal_entities = get_list_or_404(LegalEntity)

        context = {
            'owners': list(chain(physical_entities, legal_entities))
        }

        return render(request, 'owners-list.html', context)


class SingleOwnerView(TemplateView):
    def get(self, request, **kwargs):

        owner = GenericGetters.get_specific_owner(get_object_or_404(Owner, pk=kwargs.get('pk')))
        flats = []
        rooms = []
        for real_estate in owner.real_estate_property.all():
            if real_estate.real_estate_class_type == RealEstateClass.FLAT.value:
                flats.append(get_object_or_404(Flat, pk=real_estate.id))
            elif real_estate.real_estate_class_type == RealEstateClass.ROOM.value:
                rooms.append(get_object_or_404(Room, pk=real_estate.id))

        context = {
            'owner': owner,
            'flats': flats,
            'rooms': rooms
        }

        return render(request, 'single-owner.html', context)
