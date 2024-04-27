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
    name = models.CharField(max_length=50, default='')
    # email = models.CharField(max_length=80 , default="")
    # phone = models.CharField(max_length=80 , default="")
    pss = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.name
    

class Place(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    place_id = models.CharField(max_length=100, unique=True)

class PetPlace(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE)
    place_type = models.CharField(max_length=50, choices=(
        ('hospital', 'Animal Hospital/Clinic'),
        ('sitter', 'Pet Sitter'),
        ('ngo', 'Pet-related NGO')
    ))