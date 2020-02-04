from django.urls import path

from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('/', HomePageView.as_view(), name='profile'),
]