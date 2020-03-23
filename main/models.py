from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=64)
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now=True)


class Element(models.Model):
    name = models.CharField(max_length=128)
    url = models.CharField(max_length=128, default='/')
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now=True)
