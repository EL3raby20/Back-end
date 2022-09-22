from django.contrib import admin
from .models import Products,ProductsImges,Brand,Category,Reviwes

class ProductsImgeTabular(admin.TabularInline):
    model=ProductsImges

class ProductAdmin(admin.ModelAdmin):
    inlines=[ProductsImgeTabular]
    list_display=["name","quantity",'flag',"price"]
    list_filter= ["flag","brand","price"]
    search_fields=["name","subtitle"]



admin.site.register(Products,ProductAdmin)
admin.site.register(ProductsImges)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Reviwes)
