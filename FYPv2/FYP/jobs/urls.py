from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.find_job, name='job')
]