from django import forms
from django.core.exceptions import ValidationError
from shop.models import ORDER_BY_CHOICES


class ProdFiltersForm(forms.Form):
    cost__gt = forms.IntegerField(min_value=0, label="Минимальная цена", required=False)
    cost__lt = forms.IntegerField(
        min_value=0, label="Максимальная цена", required=False
    )
    order_by = forms.ChoiceField(choices=ORDER_BY_CHOICES, required=False)

    def clean(self):
        cleaned_data = super().clean()
        cost__gt = cleaned_data.get("cost__gt")
        cost__lt = cleaned_data.get("cost__lt")
        if cost__gt and cost__lt and cost__gt > cost__lt:
            raise ValidationError("Минимальная цена не может быть больше максимальной")


class PurchaseFilterForm(forms.Form):
    order_by = forms.ChoiceField(
        choices=(
            ("-created_at", "Сначала новые"),
            ("created_at", "Сначала старые"),
        ),
        required=False,
    )
