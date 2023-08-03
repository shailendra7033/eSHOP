from django.db import models
from django.contrib.auth.models import User



# Create your models here.

CATEGORY = [
    ('JNS','Jeans'),
    ('HOD','Hoddie'),
    ('M','MobilePhone'),
    ('TS','Tshirt'),
    ('JKT','Jacket'),
    ('CAP','Cap')
]

STATUS =[
    ('PND','PENDING'),
    ('DEL','DELIVERED'),
    ('SHIP','SHIPPED'),
    ('WAY','ONTHEWAY')
]

class Product(models.Model):
    name = models.CharField(max_length=70)
    price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField();
    product_image = models.ImageField(upload_to='images')
    category = models.CharField(max_length=10, choices=CATEGORY)
    def __str__(self):
        return str(self.id)



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity =models.PositiveIntegerField(default=1)
    def __str__(self):
        return str(self.id)



class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE);
    name = models.CharField(max_length=70);
    locality = models.CharField(max_length=50);
    city = models.CharField(max_length=50);
    pincode = models.BigIntegerField();
    state = models.CharField(max_length=50);
    def __str__(self):
        return str(self.id)



class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE);
    product = models.ForeignKey(Product, on_delete=models.CASCADE);
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE);
    ordered_date = models.DateField();
    quantity = models.PositiveBigIntegerField();
    status = models.CharField(choices=STATUS,max_length=10);
    def __str__(self):
        return str(self.id)


