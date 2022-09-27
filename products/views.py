from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Products,Brand,Category

class Product_List(ListView):
    model=Products


class product_Detali(DetailView):
    model=Products



class Brand_List(ListView):
    model=Brand


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["category"] =Category.objects.all() 
        return context




class Brand_Detail(DetailView):
    model=Brand

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand=self.get_object()
        context["brand_products"] =Products.objects.filter(brand=brand)
        return context
    

class Category_List(ListView):
    model=Category
    