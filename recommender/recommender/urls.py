"""recommender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from . import views

from recommender.movierecommender.views import movie_recommendation_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movierecommender/', include('movierecommender.urls')),
    #route a string that contains a URL pattern
    path(route='', view=views.movie_recommendation_view, name='recommendations')
]
