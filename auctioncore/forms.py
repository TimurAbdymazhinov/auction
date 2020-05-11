from django import forms
from .models import Auction
from category.models import *


class AuctionForm(forms.ModelForm):

    class Meta:
        model = Auction
        fields = ['category', 'subcategory', 'title', 'description', 'country', 'city', 'is_active', 'is_done',
                  'start_price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['subcategory'].queryset = SubCategory.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = SubCategory.objects.filter(owner_id=category_id).order_by('title')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategories.order_by('title')

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input'
