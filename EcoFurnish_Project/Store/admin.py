from django.contrib import admin
from .models import *
# Register your models here.



class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"link":['category',]}
admin.site.register(Categories, CategoriesAdmin)


class ItemAdmin(admin.ModelAdmin):
    search_fields = ['product', 'content', 'category__category']
    list_display = ['product', 'category', 'stock', 'price']
    list_editable = ['stock', 'price']
admin.site.register(Furniture, ItemAdmin)
