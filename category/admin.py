from django.contrib import admin
from .models import Category, SubCategory


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
