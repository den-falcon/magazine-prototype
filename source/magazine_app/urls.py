from django.urls import path

from magazine_app.views.orders import OrderCreate
from magazine_app.views.products import ProductsView, ProductCreate, ProductUpdate, ProductRead, ProductDelete
from magazine_app.views.products_in_cart import ProductInCartCreate, ProductInCartRead, ProductInCartDelete

urlpatterns = [
    path('', ProductsView.as_view(), name='index'),
    path('product/create/', ProductCreate.as_view(), name='product-create'),
    path('product/<int:pk>/', ProductRead.as_view(), name='product-read'),
    path('product/update/<int:pk>/', ProductUpdate.as_view(), name='product-update'),
    path('product/delete/<int:pk>/', ProductDelete.as_view(), name='product-delete'),
    path('product/<int:pk>/add-to-cart/', ProductInCartCreate.as_view(), name='product-add-to-cart'),
    path('product_in_cart/list/', ProductInCartRead.as_view(), name='product_in_cart-read'),
    path('product_in_cart/<int:pk>/delete/', ProductInCartDelete.as_view(), name='product_in_cart-delete'),
    path('order/create', OrderCreate.as_view(), name='order-create')
]
