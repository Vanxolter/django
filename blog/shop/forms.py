from django import forms
from django.core.exceptions import ValidationError
from shop.models import ORDER_BY_CHOICES

class ProdFiltersForm(forms.Form):
    ...