from django.db import models

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=30)
    category = models.CharField(max_length=50 , default="")
    subcategory = models.CharField(max_length=50 , default="")
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=800)

    def __str__(self):
        return self.product_name

class Login(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=80 , default="")
    phone = models.CharField(max_length=80 , default="")

    def __str__(self):
        return self.name