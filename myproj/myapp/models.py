from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SubItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    subtitle = models.CharField(max_length=200)
    subcontent = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
