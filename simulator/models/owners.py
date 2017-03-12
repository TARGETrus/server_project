from django.db import models
from simulator.utils.validators import digit_regex

GENDER = (
    ('M', 'Male'),
    ('F', 'Female')
)


class Owner(models.Model):
    phone_number = models.CharField(max_length=15, validators=[digit_regex])
    address_actual = models.CharField(max_length=200)
    address_registered = models.CharField(max_length=200)


class PhysicalEntity(Owner):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    third_name = models.CharField(max_length=100, blank=True, default='')
    gender = models.CharField(choices=GENDER, max_length=1)
    birth_date = models.DateField()
    passport_series = models.CharField(max_length=4, validators=[digit_regex])
    passport_number = models.CharField(max_length=6, validators=[digit_regex])
    passport_issued_date = models.DateField()


class LegalEntity(Owner):
    company_name = models.CharField(max_length=100)
    inn = models.CharField(max_length=12, blank=True, default='', validators=[digit_regex])
