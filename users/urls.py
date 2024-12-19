from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.urls import path
from .views import AddUserView,UserView,ListUserView
app_name = 'user'

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('add/',AddUserView.as_view(),name='addUser'),
    path('user/',UserView.as_view(),name='Userview'),
    path('list/',ListUserView.as_view(),name='addUser'),
]