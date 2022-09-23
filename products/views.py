from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Products

class Product_List(ListView):
    model=Products


class product_Detali(DetailView):
    model=Products