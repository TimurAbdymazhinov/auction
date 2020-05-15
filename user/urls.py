from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import urls
from user.views import *

urlpatterns = [
    path('accounts/login/', MyLoginView.as_view(), name='login'),
    path('accounts/', include(urls)),
    path('accounts/registration/', RegistrationView.as_view(), name='register'),

    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/favorite/', FavoriteView.as_view(), name='favorite'),
    path('profile/settings/', ProfileSettingsView.as_view(), name='profile_settings'),

    # path('', Login.as_view(), name='index'),
    # path('login/', Login.as_view(), name='login'),
    # path('reg/', Registration.as_view(), name='registration'),

]
