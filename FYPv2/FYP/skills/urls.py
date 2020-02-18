from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.SkillsList.as_view(), name='Skills_list'),
    path('view/<int:pk>', views.SkillsView.as_view(), name='Skills_view'),
    path('new', views.SkillsCreate.as_view(), name='Skills_new'),
    path('view/<int:pk>', views.SkillsView.as_view(), name='Skills_view'),
    path('edit/<int:pk>', views.SkillsUpdate.as_view(), name='Skills_edit'),
    path('delete/<int:pk>', views.SkillsDelete.as_view(), name='Skills_delete'),
]
