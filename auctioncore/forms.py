from django import forms
from .models import Auction
from category.models import *


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%dT%H:%M"
        super().__init__(**kwargs)


class AuctionForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),

    )
    subcategory = forms.ModelChoiceField(
        queryset=SubCategory.objects.all(),
        required=False
    )
    end_date = forms.DateTimeField(widget=DateTimeInput)

    class Meta:
        model = Auction
        widgets = {
            'description': forms.Textarea(attrs={'rows': 20, 'cols': 15, 'style': 'height: 200px; width: 600px;'}),

        }
        fields = ['category', 'subcategory', 'title', 'description', 'country', 'city',
                  'start_price', 'increment', 'end_date']

    def __init__(self, *args, **kwargs):
        super(AuctionForm, self).__init__(*args, **kwargs)
        self.fields["end_date"].input_formats = ["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"]

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input'
