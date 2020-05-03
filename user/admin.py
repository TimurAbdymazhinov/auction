from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["is_client", "country"]


admin.site.register(Profile, ProfileAdmin)
