
from django.urls import path

from .views import *


urlpatterns = [
    path('delete/<str:id>', AuctionDeleteView.as_view(), name='auction_delete'),
    path('edit/<str:id>', AuctionEditView.as_view(), name='auction_edit'),
    path('create/', AuctionCreateView.as_view(), name='auction_create'),

]
