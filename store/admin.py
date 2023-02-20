from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register models
admin.site.register(Products,AdminProduct)
admin.site.register(Category)
admin.site.register(Customer)






