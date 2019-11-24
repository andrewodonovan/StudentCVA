from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^createcv$', views.CvView.as_view(), name='createcv'),
    url(r'^profile$', views.profileView.as_view(), name='profile'),
]
