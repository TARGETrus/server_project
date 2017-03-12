from django.db import models
from .owners import Owner


class Flat(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.PROTECT)
    flat_type = models.CharField()
    description = models.TextField()
    new_build = models.BooleanField()
