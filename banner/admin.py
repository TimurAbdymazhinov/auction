from django.contrib import admin
from .models import Banner


class BannerAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


admin.site.register(Banner, BannerAdmin)
