from django.db import models


class Banner(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    image = models.ImageField(upload_to='banner', null=True, blank=True)

    def __str__(self):
        return self.name
