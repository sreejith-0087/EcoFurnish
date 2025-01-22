from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CustomerDetails(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.BigIntegerField(unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='Customers/', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'