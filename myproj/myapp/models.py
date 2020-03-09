from django.db import models


class Item(models.Model):
    title = models.CharField(
        verbose_name='タイトル',
        max_length=200,
        default='',
        blank=True)
    content = models.TextField(
        verbose_name='本文',
        default='',
        blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SubItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    subtitle = models.CharField(
        verbose_name='サブタイトル',
        max_length=200,
        default='',
        blank=True)
    subcontent = models.TextField(
        verbose_name='サブ本文',
        default='',
        blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
