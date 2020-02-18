from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.WorkExperienceList.as_view(), name='WorkExperience_list'),
    path('view/<int:pk>', views.WorkExperienceView.as_view(), name='WorkExperience_view'),
    path('new', views.WorkExperienceCreate.as_view(), name='WorkExperience_new'),
    path('view/<int:pk>', views.WorkExperienceView.as_view(), name='WorkExperience_view'),
    path('edit/<int:pk>', views.WorkExperienceUpdate.as_view(), name='WorkExperience_edit'),
    path('delete/<int:pk>', views.WorkExperienceDelete.as_view(), name='WorkExperience_delete'),
]
