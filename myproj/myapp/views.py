from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Item, SubItem


class IndexView(generic.ListView):
    model = Item
    template_name = 'myapp/index.html'
    context_object_name = 'latest_item_list'

    def get_queryset(self):
        """Return the last five published items."""
        return Item.objects.order_by('-created_at')[:5]


class DetailView(generic.DetailView):
    model = Item
    template_name = 'myapp/detail.html'


class ResultsView(generic.DetailView):
    model = Item
    template_name = 'myapp/results.html'