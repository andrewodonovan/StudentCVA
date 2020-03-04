from django.urls import path, include
from . import views
urlpatterns = [
    # Custom Views
    path('', views.job_search, name='job-search'),
    path('find', views.display_jobs, name='display-jobs'),
    #
    # path('', views.JobsList.as_view(), name='Jobs_list'),
    # path('view/<int:pk>', views.JobsView.as_view(), name='Jobs_view'),
    # path('new', views.JobsCreate.as_view(), name='Jobs_new'),
    # path('view/<int:pk>', views.JobsView.as_view(), name='Jobs_view'),
    # path('edit/<int:pk>', views.JobsUpdate.as_view(), name='Jobs_edit'),
    # path('delete/<int:pk>', views.JobsDelete.as_view(), name='Jobs_delete')
]