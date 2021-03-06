from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=258)
    price = models.IntegerField(default=0)
    description = models.TextField(null=True,blank=True)
    thumbnail = models.ImageField(null=True,upload_to='tnumbnails/')

    def __str__(self):
        return self.product_name
