from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'physical_entities': reverse('physicalentity-list', request=request, format=format),
        'legal_entities': reverse('legalentity-list', request=request, format=format),
        'flats': reverse('flat-list', request=request, format=format),
        'rooms': reverse('room-list', request=request, format=format),
        'prices': reverse('price-list', request=request, format=format)
    })
