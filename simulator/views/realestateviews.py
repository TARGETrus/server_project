from rest_framework import generics, permissions

from simulator.models.realestate import RealEstate, Flat, Room
from simulator.serializers.realestateserializers import RealEstateSerializer, FlatSerializer, RoomSerializer


class RealEstateDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'put', 'patch', 'delete']

    queryset = RealEstate.objects.all()
    serializer_class = RealEstateSerializer


class FlatList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post']

    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class FlatDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code snippet instance.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'put', 'patch', 'delete']

    queryset = Flat.objects.all()
    serializer_class = FlatSerializer


class RoomList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post']

    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code snippet instance.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'put', 'patch', 'delete']

    queryset = Room.objects.all()
    serializer_class = RoomSerializer
