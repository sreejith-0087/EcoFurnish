from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Cart)

admin.site.register(CartItem)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['cart_id', 'payment_type', 'amount', 'payment_status', 'delivery_status']
    list_editable = ['delivery_status']
