from django.urls import path
from .views import index, create, view, update, delete

urlpatterns = [
    path('', index, name='index'),
    path('product/create/', create, name='create'),
    path('product/<int:pk>/', view, name='view'),
    path('product/update/<int:pk>/', update, name='update'),
    path('product/delete/<int:pk>/', delete, name='delete')
]
