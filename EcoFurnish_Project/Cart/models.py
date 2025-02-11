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


class Order(models.Model):
    COD = 1
    Card = 2
    choices = (
        (1, 'Cash On Delivery'),
        (2, 'Card Payment')
    )

    user = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    address = models.TextField(max_length=300, default='my_address')
    postal_zip = models.IntegerField()
    delivery_status = models.BooleanField(default=False)
    date_time = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    quantity = models.IntegerField(default=0)
    payment_status = models.BooleanField(default=False)
    payment_type = models.IntegerField(choices=choices)

    def __str__(self):
        return f'Order Id: {self.cart_id.cart_id} - User: {self.user.first_name}'


class ProductOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Furniture, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    delivery_status = models.BooleanField(default=False)
    product_total = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    def __str__(self):
        return f'Order {self.order} Product: {self.product} Quantity: {self.quantity}'








