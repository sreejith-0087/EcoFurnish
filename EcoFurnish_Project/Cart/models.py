from django.apps.config import MODELS_MODULE_NAME
from django.db import models
from Customer.models import CustomerDetails
from Store.models import Furniture
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']
    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Furniture, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)
    class Meta:
        db_table = 'CartItem'
    def subtotal(self):
        return self.product.price * self.quantity
    def __str__(self):
        return self.product




