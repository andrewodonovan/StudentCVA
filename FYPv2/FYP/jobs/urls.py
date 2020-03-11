from django.conf.urls import url
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.job_search, name='job-search'),
    path('find', views.display_jobs, name='display-jobs'),
#   https://www.dev2qa.com/how-to-pass-parameters-to-view-via-url-in-django/
    url(r'^keywords/(?P<key>\w+)/$', views.keywords, name='keywords'),
    path('matches', views.compare_strings, name='matches'),
]