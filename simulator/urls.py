from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view

from simulator.views import views, ownersviews, realestateviews, pricesviews, dealsviews

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url('^schema/$', schema_view),
    url(r'^physical-entities/$',
        ownersviews.PhysicalEntityList.as_view(),
        name='physicalentity-list'),
    url(r'^physical-entities/(?P<pk>[0-9]+)/$',
        ownersviews.PhysicalEntityDetail.as_view(),
        name='physicalentity-detail'),
    url(r'^legal-entities/$',
        ownersviews.LegalEntityList.as_view(),
        name='legalentity-list'),
    url(r'^legal-entities/(?P<pk>[0-9]+)/$',
        ownersviews.LegalEntityDetail.as_view(),
        name='legalentity-detail'),
    url(r'^flats/$',
        realestateviews.FlatList.as_view(),
        name='flat-list'),
    url(r'^flats/(?P<pk>[0-9]+)/$',
        realestateviews.FlatDetail.as_view(),
        name='flat-detail'),
    url(r'^rooms/$',
        realestateviews.RoomList.as_view(),
        name='room-list'),
    url(r'^rooms/(?P<pk>[0-9]+)/$',
        realestateviews.RoomDetail.as_view(),
        name='room-detail'),
    url(r'^sales/$',
        dealsviews.SaleList.as_view(),
        name='sale-list'),
    url(r'^sales/(?P<pk>[0-9]+)/$',
        dealsviews.SaleDetail.as_view(),
        name='sale-detail'),
    url(r'^rents/$',
        dealsviews.RentList.as_view(),
        name='rent-list'),
    url(r'^rents/(?P<pk>[0-9]+)/$',
        dealsviews.RentDetail.as_view(),
        name='rent-detail'),
    url(r'^prices/$',
        pricesviews.PriceList.as_view(),
        name='price-list'),
    url(r'^prices/(?P<pk>[0-9]+)/$',
        pricesviews.PriceDetail.as_view(),
        name='price-detail')
])

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
