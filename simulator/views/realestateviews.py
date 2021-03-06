from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

from simulator.models.realestate import Flat, Room
from simulator.utils.genericgetters import GenericGetters


class AllFlatsView(TemplateView):
    def get(self, request, **kwargs):

        flats = Flat.objects.all()

        context = {
            'flats': flats
        }

        return render(request, 'flats-list.html', context)


class SingleFlatView(TemplateView):
    def get(self, request, **kwargs):

        flat = get_object_or_404(Flat, pk=kwargs.get('pk'))
        rooms = flat.rooms.all()
        owner = GenericGetters.get_specific_owner(flat.owner)
        flat_prices = flat.price.get_rent_prices(flat.id) if flat.for_rent else flat.price.get_sell_prices(flat.id)

        context = {
            'flat': flat,
            'rooms': rooms,
            'owner': owner,
            'flat_prices': flat_prices

        }

        return render(request, 'single-flat.html', context)


class AllRoomsView(TemplateView):
    def get(self, request, **kwargs):

        rooms = Room.objects.all()

        context = {
            'rooms': rooms
        }

        return render(request, 'rooms-list.html', context)


class SingleRoomView(TemplateView):
    def get(self, request, **kwargs):

        room = get_object_or_404(Room, pk=kwargs.get('pk'))
        flat = room.parent_flat
        owner = GenericGetters.get_specific_owner(room.owner)
        room_prices = room.price.get_rent_prices(room.id) if room.for_rent else room.price.get_sell_prices(room.id)
        flat_prices = flat.price.get_rent_prices(flat.id) if flat.for_rent else flat.price.get_sell_prices(flat.id)

        context = {
            'room': room,
            'flat': flat,
            'owner': owner,
            'room_prices': room_prices,
            'flat_prices': flat_prices,

        }

        return render(request, 'single-room.html', context)
