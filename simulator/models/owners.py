from django.db import models

from simulator.utils.enums import OwnerClass, OwnerGender
from simulator.utils.validators import digit_regex

OWNER_CLASS = (
    (OwnerClass.OWNER.value, 'Owner'),
    (OwnerClass.PHYSICAL_ENTITY.value, 'PhysicalEntity'),
    (OwnerClass.LEGAL_ENTITY.value, 'LegalEntity')
)

GENDER = (
    (OwnerGender.MALE.value, 'Male'),
    (OwnerGender.FEMALE.value, 'Female')
)


class Owner(models.Model):
    owner_class_type = models.CharField(choices=OWNER_CLASS, max_length=1, editable=False,
                                        default=OwnerClass.OWNER.value)
    phone_number = models.CharField(max_length=15, validators=[digit_regex])
    address_actual = models.CharField(max_length=200)
    address_registered = models.CharField(max_length=200)


class PhysicalEntity(Owner):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    third_name = models.CharField(max_length=100, blank=True, default='')
    gender = models.CharField(choices=GENDER, max_length=1)
    birth_date = models.DateField(null=True)
    passport_series = models.CharField(max_length=4, validators=[digit_regex])
    passport_number = models.CharField(max_length=6, validators=[digit_regex])
    passport_issued_date = models.DateField(null=True)

    def save(self, *args, **kwargs):
        self.owner_class_type = OwnerClass.PHYSICAL_ENTITY.value
        super(PhysicalEntity, self).save(*args, **kwargs)


class LegalEntity(Owner):
    company_name = models.CharField(max_length=100)
    inn = models.CharField(max_length=12, blank=True, default='', validators=[digit_regex])

    def save(self, *args, **kwargs):
        self.owner_class_type = OwnerClass.LEGAL_ENTITY.value
        super(LegalEntity, self).save(*args, **kwargs)
