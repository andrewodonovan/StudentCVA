from django.urls import path, include

from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('cv/', include('cv.urls')),
    path('education/', include('education.urls')),
    path('skills/', include('skills.urls')),
    path('workexperience/', include('workexperience.urls')),
]