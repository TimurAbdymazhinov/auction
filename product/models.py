from django.db import models
from auctioncore.models import Auction


# Create your models here.

class Product(models.Model):
    auction = models.OneToOneField(Auction, on_delete=models.CASCADE, related_name='lot')

    name = models.CharField(max_length=50, null=True, blank=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    created_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class ImageModel(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='image')
