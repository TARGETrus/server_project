from rest_framework import generics, permissions

from simulator.models.owners import PhysicalEntity, LegalEntity
from simulator.serializers.ownersserializers import PhysicalEntitySerializer, LegalEntitySerializer


class PhysicalEntityList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post']

    queryset = PhysicalEntity.objects.all()
    serializer_class = PhysicalEntitySerializer


class PhysicalEntityDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'put', 'patch', 'delete']

    queryset = PhysicalEntity.objects.all()
    serializer_class = PhysicalEntitySerializer


class LegalEntityList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post']

    queryset = LegalEntity.objects.all()
    serializer_class = LegalEntitySerializer


class LegalEntityDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'put', 'patch', 'delete']

    queryset = LegalEntity.objects.all()
    serializer_class = LegalEntitySerializer
