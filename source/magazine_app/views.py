from django.shortcuts import render, redirect

from .models import Product

from .forms import ProductForm
from .models import Product


def index(request):
    products = Product.objects.filter(remainder__gt=0).order_by('category', 'name')
    return render(request, 'index.html', context={'products': products})


def create(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'create.html', {'form': form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            description = request.POST.get('description')
            category = request.POST.get('category')
            remainder = request.POST.get('remainder')
            price = request.POST.get('price')
            new_product = Product.objects.create(name=name, description=description, category=category,
                                                 remainder=remainder, price=price)
            return redirect('')
        return render(request, 'create.html', {"form": form})
