from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from main.views import *


urlpatterns = [
    path('', MainView.as_view(), name='index'),
]
