from modeltranslation.translator import register, TranslationOptions
from .models import Page

@register(Page)
class CategoryTranslations(TranslationOptions):
    fields = ('name', 'content')


