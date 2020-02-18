from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.EducationList.as_view(), name='Education_list'),
    path('view/<int:pk>', views.EducationView.as_view(), name='Education_view'),
    path('new', views.EducationCreate.as_view(), name='Education_new'),
    path('view/<int:pk>', views.EducationView.as_view(), name='Education_view'),
    path('edit/<int:pk>', views.EducationUpdate.as_view(), name='Education_edit'),
    path('delete/<int:pk>', views.EducationDelete.as_view(), name='Education_delete'),
]
