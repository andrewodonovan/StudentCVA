"""FYP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include('pages.urls')),
    path('cv/', include('cv.urls')),
    path('education/', include('education.urls')),
    path('skills/', include('skills.urls')),
    path('workexperience/', include('workexperience.urls')),
    path('jobs/', include('jobs.urls')),
    path('users/', include('users.urls')), # new
    path('users/', include('django.contrib.auth.urls')), # new
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), # new

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)