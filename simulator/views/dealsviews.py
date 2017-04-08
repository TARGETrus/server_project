from rest_framework import generics, permissions

from simulator.models.deals import Sale, Rent
from simulator.serializers.dealsserializer import SaleSerializer, RentSerializer


class SaleList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post']

    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class SaleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'put', 'patch', 'delete']

    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class RentList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post']

    queryset = Rent.objects.all()
    serializer_class = RentSerializer


class RentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'put', 'patch', 'delete']

    queryset = Rent.objects.all()
    serializer_class = RentSerializer
