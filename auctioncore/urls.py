from django.urls import path

from .views import *

urlpatterns = [
    path('list/<str:type>/<str:id>', AuctionsView.as_view(), name='auctions'),
    path('delete/<str:id>', AuctionDeleteView.as_view(), name='auction_delete'),
    path('part/delete/<str:id>', ParticipantsDeleteView.as_view(), name='auction_participants_delete'),
    path('edit/<str:id>', AuctionEditView.as_view(), name='auction_edit'),
    path('detail/<str:id>', AuctionDetailView.as_view(), name='auction_detail'),
    path('bet/<str:id>', AuctionMakeBetView.as_view(), name='make_bet'),
    path('comment/<str:id>', AuctionCommentView.as_view(), name='comment'),

    path('create/', AuctionCreateView.as_view(), name='auction_create'),

    path('ajax/load-subcategories/', loadSubCategories, name='ajax_load_subcategories'),
    path('ajax/sort-auctions/', loadAuctionsBy, name='ajax_sort_auctions'),

]
