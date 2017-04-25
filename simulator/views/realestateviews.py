from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.views.generic import TemplateView

from simulator.models.realestate import Flat, Room


class AllFlatsView(TemplateView):
    def get(self, request, **kwargs):

        flats = get_list_or_404(Flat)

        context = {'flats': flats}

        return render(request, 'flats-list.html', context)


class SingleFlatView(TemplateView):
    def get(self, request, **kwargs):

        flat = get_object_or_404(Flat, pk=kwargs.get('pk'))

        context = {'flat': flat}

        return render(request, 'single-flat.html', context)


class AllRoomsView(TemplateView):
    def get(self, request, **kwargs):

        rooms = get_list_or_404(Room)

        context = {'rooms': rooms}

        return render(request, 'rooms-list.html', context)


class SingleRoomView(TemplateView):
    def get(self, request, **kwargs):

        room = get_object_or_404(Room, pk=kwargs.get('pk'))

        context = {'room': room}

        return render(request, 'single-room.html', context)
