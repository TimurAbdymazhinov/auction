from django.db import models
from auctioncore.models import Auction
from category.models import Category
from user.models import Profile


class Image(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='images', null=True,
                                blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='images', null=True,
                                 blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


class Images(models.Model):
    owner = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='image')
