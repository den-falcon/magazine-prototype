from django.contrib import admin

# Register your models here.

from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    list_filter = ['name']
    search_fields = ['name', 'category']
    fields = ['name', 'description', 'category', 'remainder', 'price']
    # readonly_fields = ['created_at', 'updated_at']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)

