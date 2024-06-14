"""
URL configuration for Backend_pawfetch project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
)
from PawfetchMatch_app.views import *
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', get_profile, name='get-profile'),
    path('create-user/', create_user, name='create-user'),
    path('update-user/', update_user, name='update_user'),
    path('delete-user/', delete_user, name='delete_user'),
    path('create-listing/', create_listing, name='create-listing'),
    path('update-listing/', update_listing, name='update-listing'),
    path('delete-listing/', delete_listing, name='delete-listing'),
    path('get-listing/', get_listing, name='get-listing'),
    path('create-message/', create_message, name='create-message'),
    path('update-message/', update_message, name='update-message'),
    path('delete-message/', delete_message, name='delete-message'),
    path('get-message/', get_message, name='get-message'),
    path('logout/', logout, name='logout'),
    path('token/', TokenObtainPairView.as_view()),
]

if settings.DEBUG: 
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)