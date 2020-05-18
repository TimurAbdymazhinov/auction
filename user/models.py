from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_client = models.BooleanField(default=False)
    is_auction_owner = models.BooleanField(default=False)
    image = models.ImageField(upload_to='user',
                              verbose_name='Фотография', null=True, blank=True)
    country = models.CharField(max_length=200, verbose_name='Страна', null=True, blank=True)
    city = models.CharField(max_length=200, verbose_name='Город', null=True, blank=True)
    phone = models.CharField(max_length=200, verbose_name='Номер телефона', null=True, blank=True)

    is_active = models.BooleanField(default=True)

    star = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
