from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from user.views import *


urlpatterns = [
    # path('', Login.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('reg/', Registration.as_view(), name='registration'),

]
