from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics, permissions, renderers
from django.contrib.auth.models import User
from simulator.models.snippets import Snippet
from simulator.serializers.serializers import SnippetSerializer, UserSerializer
from simulator.permissions import IsOwnerOrReadOnly


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format),
        'physical_entities': reverse('physical-entity-list', request=request, format=format),
        'legal_entities': reverse('legal-entity-list', request=request, format=format),
        # 'flats': reverse('flat-list', request=request, format=format),
        # 'rooms': reverse('room-list', request=request, format=format)
    })


class SnippetList(generics.ListCreateAPIView):
    """
    List all code snippets, or create a new code snippet instance.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    http_method_names = ['get', 'post']

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code snippet instance.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    http_method_names = ['get', 'put', 'patch', 'delete']

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetHighlight(generics.GenericAPIView):
    http_method_names = ['get']

    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


class UserList(generics.ListAPIView):
    http_method_names = ['get']

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    http_method_names = ['get']

    queryset = User.objects.all()
    serializer_class = UserSerializer
