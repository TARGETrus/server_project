from rest_framework import generics, permissions
from simulator.models.realestate import Flat, Room
from simulator.serializers.realestateserializers import FlatSerializer, RoomSerializer
from simulator.permissions import IsOwnerOrReadOnly


class FlatList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    http_method_names = ['get', 'post']

    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class RoomList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    http_method_names = ['get', 'post']

    queryset = Room.objects.all()
    serializer_class = RoomSerializer
