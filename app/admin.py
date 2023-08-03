from django.contrib import admin;
from django.db import models;
from .models import Product,Cart,Customer,OrderPlaced;



# Register your models here.
@admin.register(Product)
class product(admin.ModelAdmin):
    list_display=('name','price','discount_price','description','product_image','category')


@admin.register(Cart)
class cart(admin.ModelAdmin):
    list_display=('id','user','product','quantity')

@admin.register(Customer)
class customer(admin.ModelAdmin):
    list_display=('id','user','name','locality','city','pincode','state')

@admin.register(OrderPlaced)
class ordered(admin.ModelAdmin):
    list_display =('user','customer','product','ordered_date','quantity','status')
