
from itertools import count
from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Products,Brand,Category
from django.db.models import Q, F , Value
from django.db.models.aggregates import Count, Min,Max,Sum,Avg
from django.db.models.functions import  Concat

'''' '''''''
 
    def product_test(request):

    
     product=Products.objects.filter(
       Q (name__endswith="on") | Q (quantity__gte=800))
    product=Products.objects.filter(price=F("quantity"))

    product=Products.objects.filter(price__gt=40)
    product=Products.objects.filter(price__lt=40)
    product=Products.objects.filter(price__lte=40)

    product=Products.objects.filter(price__range=(500,100))

    product=Products.objects.filter(name__statswithe="on")
    product=Products.objects.filter(name__endswith="th")

    product=Products.objects.order_by("name") عشان يرتب الحروف الابجدي  من الاول
    product=Products.objects.order_by("-name") عشان يرتب الحروف الابجدي  من الاخر
    product=Products.objects.order_by("name", "price")

     product=Products.objects.filter(name__endswith="on").order_by("name")  

     product=Products.objects.filter(price__range=(500,1000)).order_by("subtitle")

      product=Products.objects.earliest("name") هتجيب اول واحد بس
      product=Products.objects.latest("name") هتجيب اخر واحد بس 

      product=Products.objects.all()[10:100]

      product=Products.objects.all()  لو احنا استخدمنا ال all 
      ككل هيعمل كويري كتير جدا ف احنا عشان نظبط الموضوع دا 


    product=Products.objects.valus("name","price") عشان يرجع اسامي اعمده بس
    product=Products.objects.valus_list() عشان يرجع اسامي اعمده بس
    product=Products.objects.only("name") لو استخدمنا only 
    الازم نتاكد اننا مستدعينها ف صفحه ال اتش دي ام ال عشان مينفذش كواري كتير جدا

    one-to-one or one-to-many use ----->
    product=Products.objects.select_related("category").all()  # select_related

    many to many use -------- >
    product=Products.objects.prefetch_related.all()          #prefetch_related

     product=Products.objects.aggregate(Count("quantity"))
      #product=Products.objects.aggregate(Sum("quantity"))

      product=Products.objects.select_related("category").annotate(info=Value("name")) كدا ضافلي عمود جديد هرجع بيه 

   # product=Products.objects.select_related("category").annotate(info=Concat("name","flag"))

    product=Products.objects.all()

 
    return render (request,"products/product_list_test.html",{"product":product})

 '''
class Product_List(ListView):
    model=Products
    paginate_by=30

class product_Detali(DetailView):
    model=Products



class Brand_List(ListView):
    model=Brand


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["category"] =Category.objects.all() 

        context["brand_list"]=Brand.objects.all().annotate(p_count=Count('product_brand'))
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
    