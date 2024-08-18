from django.urls import path
from .views import *


urlpatterns = [
    path('reg', user_registraion, name="reg"),
    path('login', user_login, name="log in"),
    path('logout', user_logout, name="log out"),
]
