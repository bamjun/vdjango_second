from django.contrib import admin
from django.contrib.admin.sites import site

from .models import Category, Product

admin.site.register(Category)
admin.site.register(Product)

# Register your models here.
