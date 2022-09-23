from django.urls import path
from products.views import Product_List,product_Detali

app_name="products"

urlpatterns = [
    path('', Product_List.as_view(),name="Product_List"),
    path('<int:pk>', product_Detali.as_view(),name="product_Detali"),


]