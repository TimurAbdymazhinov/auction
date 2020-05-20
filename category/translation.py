from modeltranslation.translator import register, TranslationOptions
from .models import Category, SubCategory


@register(Category)
class CategoryTranslations(TranslationOptions):
    fields = ('title', )


@register(SubCategory)
class SubCategoryTranslations(TranslationOptions):
    fields = ('title', )


