from django import forms
from django.forms import widgets
from magazine_app.models import Product, Cart, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        exclude = ['product']
        # widgets = {
        #     'count': forms.IntegerField(attrs={'class': 'form-control rounded-0', 'style': 'max-width: 50px;'})
        # }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти",
                             widget=widgets.TextInput(attrs={'class': 'form-control'}))


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'address']
