from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from user.views import *

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration', RegistrationView.as_view(), name='register'),

    path('profile/', ProfileView.as_view(), name='profile'),

    # path('', Login.as_view(), name='index'),
    # path('login/', Login.as_view(), name='login'),
    # path('reg/', Registration.as_view(), name='registration'),

]
