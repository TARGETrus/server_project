from django.shortcuts import get_object_or_404

from simulator.models.owners import PhysicalEntity, LegalEntity
from simulator.models.realestate import Flat, Room
from simulator.models.deals import Sale, Rent
from simulator.utils.enums import OwnerClass
from simulator.utils.enums import RealEstateClass
from simulator.utils.enums import DealClass


class GenericGetters(object):

    @staticmethod
    def get_specific_owner(owner):
        if owner.owner_class_type == OwnerClass.PHYSICAL_ENTITY.value:
            return get_object_or_404(PhysicalEntity, pk=owner.id)
        elif owner.owner_class_type == OwnerClass.LEGAL_ENTITY.value:
            return get_object_or_404(LegalEntity, pk=owner.id)

    @staticmethod
    def get_specific_deal(deal):
        if deal.deal_class_type == DealClass.SALE.value:
            return get_object_or_404(Sale, pk=deal.id)
        elif deal.deal_class_type == DealClass.RENT.value:
            return get_object_or_404(Rent, pk=deal.id)

    @staticmethod
    def get_specific_restate(real_estate):
        if real_estate.real_estate_class_type == RealEstateClass.FLAT.value:
            return get_object_or_404(Flat, pk=real_estate.id)
        elif real_estate.real_estate_class_type == RealEstateClass.ROOM.value:
            return get_object_or_404(Room, pk=real_estate.id)
