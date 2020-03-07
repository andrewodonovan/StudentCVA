from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.job_search, name='job-search'),
    path('find', views.display_jobs, name='display-jobs'),
]