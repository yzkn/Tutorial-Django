from django.db import models


class Item(models.Model):
    item_title = models.CharField(max_length=200)
    item_content = models.CharField(max_length=200)


class SubItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    subtitle = models.CharField(max_length=200)
    subcontent = models.CharField(max_length=200)
