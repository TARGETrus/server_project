from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from simulator.views import views, ownersviews, realestateviews, pricesviews, dealsviews


urlpatterns = format_suffix_patterns([
    url(r'^admin/', admin.site.urls),
    url(r'^$',
        views.IndexView.as_view(),
        name='index'),
    url(r'^owners/$',
        ownersviews.AllOwnersView.as_view(),
        name='owner-list'),
    url(r'^owners/(?P<pk>[0-9]+)/$',
        ownersviews.SingleOwnerView.as_view(),
        name='owner-detail'),
    url(r'^flats/$',
        realestateviews.AllFlatsView.as_view(),
        name='flat-list'),
    url(r'^flats/(?P<pk>[0-9]+)/$',
        realestateviews.SingleFlatView.as_view(),
        name='flat-detail'),
    url(r'^rooms/$',
        realestateviews.AllRoomsView.as_view(),
        name='room-list'),
    url(r'^rooms/(?P<pk>[0-9]+)/$',
        realestateviews.SingleRoomView.as_view(),
        name='room-detail'),
])
