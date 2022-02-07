from django.urls import path
from magazine_app.views.products import ProductsView, ProductCreate, ProductUpdate, ProductRead, ProductDelete

urlpatterns = [
    path('', ProductsView.as_view(), name='index'),
    path('product/create/', ProductCreate.as_view(), name='product-create'),
    path('product/<int:pk>/', ProductRead.as_view(), name='product-read'),
    path('product/update/<int:pk>/', ProductUpdate.as_view(), name='product-update'),
    path('product/delete/<int:pk>/', ProductDelete.as_view(), name='product-delete')
]
