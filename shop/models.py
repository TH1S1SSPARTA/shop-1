from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 66)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    price = models.PositiveIntegerField()
    rating = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    stcok = models.IntegerField()
    sales = models.BooleanField()