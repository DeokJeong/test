from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from .views import RegisterView, UserView



urlpatterns = [
    path('users/', UserView.as_view()),
    path('users/<int:pk>', UserView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', obtain_jwt_token),
    path('token/refresh', refresh_jwt_token),
    path('token/verify', verify_jwt_token),
]