from django.db import models

# Create your models here.

class Categories(models.Model):
    category = models.CharField(max_length=30, unique=True)
    link = models.SlugField(unique=True)
    def __str__(self):
        return self.category

class Furniture(models.Model):
    product = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=1000, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='Furniture')
    stock = models.IntegerField()

    def __str__(self):
        return self.product

