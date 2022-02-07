from django import forms
from django.forms import widgets
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти",
                             widget=widgets.TextInput(attrs={'class': 'form-control'}))



