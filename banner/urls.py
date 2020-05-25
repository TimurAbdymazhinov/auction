from django.urls import path

from .views import *

urlpatterns = [
    path('aboutAuctions/', AboutAuctionsView.as_view(), name='page_aboutAuctions'),
    path('contacts/', ContactsView.as_view(), name='page_contacts'),
    path('aboutUs/', AboutUsView.as_view(), name='page_aboutUs'),


]
