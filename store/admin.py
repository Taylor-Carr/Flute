from django.contrib import admin
from .models import Category, Customer, Product, Order, ProductImage, ProductCustomization, Benefit

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


    

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(ProductCustomization)
admin.site.register(Benefit)