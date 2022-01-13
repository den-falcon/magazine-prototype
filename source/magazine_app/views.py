from django.shortcuts import render, redirect, get_object_or_404

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
            return redirect('view', pk=new_product.pk)
        return render(request, 'create.html', {"form": form})


def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(initial={
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'remainder': product.remainder,
            'price': product.price
        })
        return render(request, 'update.html', context={'product': product, 'form': form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = request.POST.get('name')
            product.description = request.POST.get('description')
            product.category = request.POST.get('category')
            product.remainder = request.POST.get('remainder')
            product.price = request.POST.get('price')
            product.save()
            return redirect('view', pk=product.pk)
        return render(request, 'update.html', context={'product': product, 'form': form})


def view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'view.html', context={'product': product})
