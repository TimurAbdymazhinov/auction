
from django.urls import path

from .views import *


urlpatterns = [
    path('delete/<str:id>', AuctionDeleteView.as_view(), name='auction_delete'),
]
