from django.contrib import admin
from .models import cart, cart_Detail , Order, Order_Detail

class orderadmin(admin.ModelAdmin):
    list_display=["user","states"]
    search_fields=[]
    list_filter=[]

admin.site.register(cart,orderadmin)
admin.site.register(cart_Detail,orderadmin)
admin.site.register(Order,orderadmin)
admin.site.register(Order_Detail,orderadmin)