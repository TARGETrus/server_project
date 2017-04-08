from rest_framework import generics, permissions

from simulator.models.prices import Price
from simulator.serializers.priceserializers import PriceSerializer


class PriceList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post']

    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class PriceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'put', 'patch', 'delete']

    queryset = Price.objects.all()
    serializer_class = PriceSerializer
