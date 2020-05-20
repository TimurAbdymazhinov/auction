from django.contrib import admin
from .models import Category, SubCategory

from modeltranslation.admin import TranslationAdmin


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ["title"]


@admin.register(SubCategory)
class SubCategoryAdmin(TranslationAdmin):
    list_display = ["title"]


# admin.site.register(Category, CategoryAdmin)
# admin.site.register(SubCategory, SubCategoryAdmin)
