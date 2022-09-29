from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext as _
from utils.generator_code import generat_code
from products.models import Products


cart_options=(


    ("processed","processed"),
    ("completed","completed"),

)

class cart (models.Model):
    code=models.CharField(max_length=9,default=generat_code())
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_cart")
    states=models.CharField(_("States"),choices=cart_options,max_length=20)


    def __str__(self):
        return self.code



    def get_total(self):
        total=0
        for prodct in self.cart_detail.all():
            total+=prodct.total
        return total    


class cart_Detail(models.Model):
    order=models.ForeignKey(cart,related_name="cart_detail",on_delete=models.CASCADE)
    product=models.ForeignKey(cart,on_delete=models.SET_NULL,null=True,blank=True,related_name="product_cart")
    price=models.FloatField()
    quantity=models.IntegerField()
    total=models.FloatField(null=True,blank=True)


    def __str__(self):
        return str(self.order)



states_options=(

    ("recieved","recieved"),
    ("processed","processed"),
    ("shipped","shipped"),
    ("delivered","delivered"),
)

class Order(models.Model):
    code=models.CharField(max_length=9,default=generat_code())
    user=models.ForeignKey(User,verbose_name="User",related_name="user_order",on_delete=models.CASCADE)
    states=models.CharField(_("States"),choices=states_options,max_length=20)
    order_time=models.DateTimeField(_("order_time"),default=timezone.now)
    delivery_time=models.DateTimeField(_("delivery_time"),null=True,blank=True)
    
    def __str__(self):
        return self.code


class Order_Detail(models.Model):
    order=models.ForeignKey(Order,related_name="order_detail",on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.SET_NULL,null=True,blank=True,related_name="product_order")
    price=models.FloatField()
    quantity=models.IntegerField()

    def __str__(self):
        return str(self.order)


