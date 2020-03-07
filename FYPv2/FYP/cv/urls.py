from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.CvList.as_view(), name='Cv_list'),
    path('view/<int:pk>', views.CvView.as_view(), name='Cv_view'),
    path('new', views.CvCreate.as_view(), name='Cv_new'),
    path('view/<int:pk>', views.CvView.as_view(), name='Cv_view'),
    path('edit/<int:pk>', views.CvUpdate.as_view(), name='Cv_edit'),
    path('delete/<int:pk>', views.CvDelete.as_view(), name='Cv_delete'),

    path('upload-cv', views.simple_upload, name='upload_cv'),
    path('display-cv', views.pdf_view, name='display-cv'),



]
