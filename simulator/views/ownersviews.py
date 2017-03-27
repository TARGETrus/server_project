from rest_framework import generics, permissions

from simulator.models.owners import Owner, PhysicalEntity, LegalEntity
from simulator.serializers.ownersserializers import OwnerSerializer, PhysicalEntitySerializer, LegalEntitySerializer


class OwnerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'put', 'patch', 'delete']

    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class PhysicalEntityList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post']

    queryset = PhysicalEntity.objects.all()
    serializer_class = PhysicalEntitySerializer


class PhysicalEntityDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code snippet instance.
    """
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
    """
    Retrieve, update or delete a code snippet instance.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'put', 'patch', 'delete']

    queryset = LegalEntity.objects.all()
    serializer_class = LegalEntitySerializer
