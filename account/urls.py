from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterUserView, DetailsUserView, UpdateUserView, DeleteUserView, ChangePasswordView


urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('register/', RegisterUserView.as_view()),
    path('my-profile/', DetailsUserView.as_view()),
    path('profile/<str:email>/', DetailsUserView.as_view()),
    path('update/', UpdateUserView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),
    path('delete/', DeleteUserView.as_view()),
]
