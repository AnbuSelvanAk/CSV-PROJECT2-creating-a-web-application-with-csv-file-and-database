from django.contrib import admin
from csvapp.models import Product
class ProductAdmin(admin.ModelAdmin):
	list_display=['no','name','price','warrenty','stock']
admin.site.register(Product,ProductAdmin)