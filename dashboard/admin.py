from dashboard.models import Product
from django.contrib import admin
from .models import Product
from django.contrib.auth.models import Group
from .models import Order
from .models import Supplier

admin.site.site_header = 'Inventory Dashboard'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','quantity','category',) 
    list_filter = ['category']

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Supplier)

# admin.site.unregister(Group)  # remove group in admin panel