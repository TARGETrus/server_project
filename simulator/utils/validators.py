from django.core.validators import RegexValidator


digit_regex = RegexValidator(regex=r'^\d+$', message="Only digits allowed in this field!")
