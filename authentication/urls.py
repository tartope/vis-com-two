from django.contrib import admin
from django.urls import path, include
from authentication import views

# actions/methods found in views.py:
urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('log_in', views.log_in, name='log_in'),
    path('logOut', views.logOut, name='logOut'),
]