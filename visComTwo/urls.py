"""visComTwo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from the directory import views
from visComTwo import views
from rest_framework.urlpatterns import format_suffix_patterns

# actions/methods found in views.py:
urlpatterns = [
    path('admin/', admin.site.urls),
    # get all: create a new path; give it a path name, and pass in function name from views
    path('visual_cards/', views.visual_card_list),
    # get 1 visual card
    path('visual_cards/<int:id>', views.visual_card_detail),
    # includes the urls created in the authentication directory
    path('', include('authentication.urls')),
]

# gives the above urls different extensions; whatever this returns, it replaces the urlpatterns variable; changes the view in the browser (also add 'format=None' parameter in views)
# import this above
urlpatterns = format_suffix_patterns(urlpatterns)
