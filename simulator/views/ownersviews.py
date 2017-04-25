from itertools import chain

from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.views.generic import TemplateView

from simulator.models.owners import Owner, PhysicalEntity, LegalEntity
from simulator.utils.enums import OwnerClass


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

        owner = get_object_or_404(Owner, pk=kwargs.get('pk'))

        if owner.owner_class_type == OwnerClass.PHYSICAL_ENTITY.value:
            owner = get_object_or_404(PhysicalEntity, pk=kwargs.get('pk'))
        elif owner.owner_class_type == OwnerClass.LEGAL_ENTITY.value:
            owner = get_object_or_404(LegalEntity, pk=kwargs.get('pk'))

        context = {'owner': owner}

        return render(request, 'single-owner.html', context)
