"""CinemaTicketsReservation_API URL Configuration

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
from django.urls import path , include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('guests',viewsets_guest)
router.register('movies',viewsets_movie)

urlpatterns = [
    path('norestnomodel',no_rest_no_model ),
    path('norestmodel',no_restmodel ),
    path('FBV_list',FBV_list ),
    path('FBV_pk/<int:pk>',FBV_pk ),   
    path('CBV_list',CBV_list.as_view() ),
    path('CBV_pk/<int:pk>',CBV_pk.as_view() ),
    path('mixins_list',mixins_list.as_view() ),
    path('mixins_pk/<int:pk>',mixins_pk.as_view() ),  
    path('generics_list',generics_list.as_view() ),
    path('generics_pk/<int:pk>',generics_pk.as_view() ),
    path('viewsets_guests/',include(router.urls)  ),
    path('viewsets_movies/',include(router.urls)  ),
    path('find_movie/',find_movie),
    path('api_auth',include('rest_framework.urls')),
    path('api_token_auth',obtain_auth_token),
    # path('post_list',generics_post.as_view() ),
    path('post_pk/<int:pk>',post_pk.as_view() ),
]

















