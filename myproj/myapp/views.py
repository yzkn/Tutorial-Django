from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Item, SubItem
from .forms import ItemForm, SubItemForm


class ItemListView(ListView):
    """
    GET(全件)
    templates\myapp\モデル_list.htmlを使用
    """
    model = Item
    paginate_by = 10  # ページネーション(10件ごとに表示)


class ItemDetailView(DetailView):
    """
    GET(a record)
    templates\myapp\モデル_detail.htmlを使用
    """
    model = Item


class ItemCreateView(CreateView):
    """
    POST用画面
    templates\myapp\モデル_form.htmlを使用
    """
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('myapp:item_list')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, 'Created: {}'.format(form.instance))
        return result


class ItemUpdateView(UpdateView):
    """
    PUT用画面
    templates\myapp\モデル_form.htmlを使用
    """
    model = Item
    form_class = ItemForm

    success_url = reverse_lazy('myapp:item_list')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, 'Updated: {}'.format(form.instance))
        return result


class ItemDeleteView(DeleteView):
    """
    DELETE用画面
    templates\myapp\モデル_confirm_delete.htmlを使用
    """
    model = Item
    form_class = ItemForm

    success_url = reverse_lazy('myapp:item_list')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, 'Removed: {}'.format(self.object))
        return result
