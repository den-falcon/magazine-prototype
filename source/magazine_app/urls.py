from django.urls import path
from .views import index, create

urlpatterns = [
    path('', index, name='index'),
    path('product/create/', create, name='create'),
]
