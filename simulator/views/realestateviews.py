from rest_framework import generics, permissions
from simulator.models.owners import PhysicalEntity, LegalEntity
from simulator.serializers.ownersserializers import PhysicalEntitySerializer, LegalEntitySerializer
from simulator.permissions import IsOwnerOrReadOnly


class PhysicalEntityList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    http_method_names = ['get', 'post']

    queryset = PhysicalEntity.objects.all()
    serializer_class = PhysicalEntitySerializer


class LegalEntityList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    http_method_names = ['get', 'post']

    queryset = LegalEntity.objects.all()
    serializer_class = LegalEntitySerializer
