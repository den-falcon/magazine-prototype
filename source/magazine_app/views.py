from django.shortcuts import render, redirect

from .models import Product


def index(request):
    products = Product.objects.filter(remainder__gt=0).order_by('category', 'name')
    return render(request, 'index.html', context={'products': products})
