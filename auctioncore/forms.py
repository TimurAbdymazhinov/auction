from django import forms
from .models import Auction
from category.models import *


class AuctionForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),

    )
    subcategory = forms.ModelChoiceField(
        queryset=SubCategory.objects.all(),
        required=False
    )

    class Meta:
        model = Auction
        widgets = {
            'description': forms.Textarea(attrs={'rows': 20, 'cols': 15, 'style':  'height: 200px; width: 600px;'}),
        }
        fields = ['category', 'subcategory', 'title', 'description', 'country', 'city', 'is_active', 'is_done',
                  'start_price', 'increment']

    def __init__(self, *args, **kwargs):
        super(AuctionForm, self).__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input'
