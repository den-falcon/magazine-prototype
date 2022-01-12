from django import forms
from django.forms import widgets
from .models import CATEGORY_CHOICES


class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, label='Название')
    description = forms.CharField(max_length=2000, required=True, label="Описание",
                                  widget=widgets.Textarea(attrs={"rows": 5, "cols": 50}))
    category = forms.CharField(max_length=200, required=True, label='Категория',
                               widget=widgets.Select(choices=CATEGORY_CHOICES))
    remainder = forms.IntegerField(min_value=0, required=True, label='Остаток')
    price = forms.DecimalField(min_value=1, max_digits=9, decimal_places=2, required=True, label='Стоимость')
