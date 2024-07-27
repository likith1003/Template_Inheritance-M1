from django.urls import path
from . views import *
urlpatterns = [
    path('', home, name='home'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('users', users, name='users'),
]
