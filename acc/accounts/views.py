from django.shortcuts import render

from rest_framework import generics
from .serializers import UserSerializer

from rest_framework.response import Response
from django.contrib.auth import login
from .serializers import LoginSerializer
#Sign up
class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    
#Sign in and forgot password
class CustomLoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        request.session['username'] = user.username  # Lưu tên người dùng vào session
        return Response({"message": "Logged in successfully"}, status=200)

#Quan li thong tin tai khoan
class UserDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
