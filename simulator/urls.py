from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view
from simulator.views import views, realestateviews

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url('^schema/$', schema_view),
    url(r'^snippets/$',
        views.SnippetList.as_view(),
        name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail'),
    url(r'^physical-entities/$',
        realestateviews.PhysicalEntityList.as_view(),
        name='physical-entities-list'),
    url(r'^legal-entities/$',
        realestateviews.LegalEntityList.as_view(),
        name='legal-entities-list'),
])

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
