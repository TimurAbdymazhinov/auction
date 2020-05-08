
from django.urls import path

from .views import *


urlpatterns = [
    path('delete/<str:id>', AuctionDeleteView.as_view(), name='auction_delete'),
    path('edit/<str:id>', AuctionEditView.as_view(), name='auction_edit'),
    path('detail/<str:id>', AuctionDetailView.as_view(), name='auction_detail'),
    path('bet/<str:id>', AuctionMakeBetView.as_view(), name='make_bet'),
    path('create/', AuctionCreateView.as_view(), name='auction_create'),

]
