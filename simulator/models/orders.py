from django.db import models

from simulator.utils.validators import digit_regex


class Order(models.Model):
    client_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, validators=[digit_regex])
    description = models.TextField()
