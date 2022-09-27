from django.urls import path
from products.views import Product_List,product_Detali,Brand_List,Brand_Detail,Category_List

app_name="products"

urlpatterns = [
    path('', Product_List.as_view(),name="Product_List"),
    path('<int:pk>', product_Detali.as_view(),name="product_Detali"),
    path('brand/', Brand_List.as_view(),name="Brand_List"),
    path('brand/<int:pk>', Brand_Detail.as_view(),name="Brand_Detali"),
    path('category/', Category_List.as_view(),name="Category_List")



]