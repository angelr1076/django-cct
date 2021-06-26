
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from . import views
from .views import CreateProfileView, EditProfileView, ProfileView


urlpatterns = [
    # User auth
    path('register/', views.register, name='register'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    
    # Officers
    path('officers', views.officers, name='officers'),
        
    #  # User profile
    path('createprofile/', CreateProfileView.as_view(), name='createprofile'),
    path('<int:pk>/editprofile/', EditProfileView.as_view(), name='editprofile'),
    path('<int:pk>/profile/', ProfileView.as_view(), name='profile'),
]
