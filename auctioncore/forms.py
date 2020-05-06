from django.forms import ModelForm

from .models import Auction


class AuctionForm(ModelForm):
    class Meta:
        model = Auction
        fields = ['category', 'title', 'description', 'country', 'city', 'is_active', 'is_done', 'start_price']

    def __init__(self, *args, **kwargs):
        super(AuctionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input'

