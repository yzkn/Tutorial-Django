from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'myapp'

urlpatterns = [
    url(r'^$',
        views.ItemListView.as_view(),
        name='item_list'),

    url(r'^detail/(?P<pk>\d+)/$',
        views.ItemDetailView.as_view(),
        name='item_detail'),

    url(r'^create/$',
        views.ItemCreateView.as_view(),
        name='item_create'),

    url(r'^update/(?P<pk>\d+)/$',
        views.ItemUpdateView.as_view(),
        name='item_update'),

    url(r'^delete/(?P<pk>\d+)/$',
        views.ItemDeleteView.as_view(),
        name='item_delete'),
]
