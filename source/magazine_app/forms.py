from django import forms
from django.forms import widgets
from .models import Product, ProductInCart


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []


class ProductInCartForm(forms.ModelForm):
    class Meta:
        model = ProductInCart
        exclude = ['product']
        # widgets = {
        #     'count': forms.IntegerField(attrs={'class': 'form-control rounded-0', 'style': 'max-width: 50px;'})
        # }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти",
                             widget=widgets.TextInput(attrs={'class': 'form-control'}))



