from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from simulator.views import views, ownersviews, realestateviews, dealsviews, ordersviews


urlpatterns = [
    url(r'^login/$', auth_views.login,
        {'template_name': 'login.html'},
        name='login'),
    url(r'^logout/$', auth_views.logout,
        {'template_name': 'logout.html', 'next_page': '/simulator/login/'},
        name='logout'),

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

    url(r'^deals/$',
        dealsviews.AllDealsView.as_view(),
        name='deal-list'),
    url(r'^deals/(?P<pk>[0-9]+)/$',
        dealsviews.SingleDealView.as_view(),
        name='deal-detail'),

    url(r'^orders/$',
        ordersviews.AllOrdersView.as_view(),
        name='order-list'),
]
