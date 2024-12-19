from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from .serializers import UserSerializer
from users.models import CustomUser

class AddUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser
    authentication_classes = []
    permission_classes  = [AllowAny]    

class UserView(generics.DestroyAPIView,generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser
    authentication_classes = [JWTAuthentication]
    permission_classes  = [IsAuthenticated]

class ListUserView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser
    authentication_classes = [JWTAuthentication]
    permission_classes  = [IsAdminUser]