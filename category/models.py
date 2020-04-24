from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    order = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_accepted = models.BooleanField(default=True)

    owner = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='subcategories', null=True, blank=True)

    def __str__(self):
        return self.title
