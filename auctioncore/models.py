import datetime

from django.contrib.auth.models import User
from django.db import models
from category.models import Category, SubCategory


class Auction(models.Model):
    PR = (
        (1, '1%'),
        (2, '2%'),
        (3, '3%'),
        (4, '4%'),
        (5, '5%'),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auctions')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='auctions')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='auctions', null=True,
                                    blank=True)

    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=200, verbose_name='Страна', null=True, blank=True)
    city = models.CharField(max_length=200, verbose_name='Город', null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_done = models.BooleanField(default=False)

    start_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    increment = models.IntegerField(blank=True, null=True, choices=PR)

    created_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    last_bet = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    next_bet = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    star = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


class Participants(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='participants')
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='participants')
    bet = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bed_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-bed_date']


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite')
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='favorite')


class Acomments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    star = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['-created_date']
