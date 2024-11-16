# accounts/urls.py
from django.urls import path
from .views import RegisterView
from .views import CustomLoginView
from django.contrib.auth.views import PasswordChangeView
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', UserDetailView.as_view(), name='profile'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
]
