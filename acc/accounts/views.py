from django.shortcuts import render, redirect 
from django.contrib import messages

from rest_framework import generics
from .serializers import UserSerializer

from rest_framework.response import Response
from django.contrib.auth import login
from .serializers import LoginSerializer

from django.contrib.auth.views import PasswordChangeView 
from django.urls import reverse_lazy
#Sign up
class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    
    def post(self, request, *args, **kwargs): 
        serializer = self.get_serializer(data=request.data) 
        serializer.is_valid(raise_exception=True) 
        serializer.save() 
        messages.success(request, 'Đăng ký thành công! Vui lòng kiểm tra email để xác thực tài khoản.') 
        return redirect('login') # Chuyển hướng đến trang đăng nhập sau khi đăng ký thành công
#Sign in and forgot password
class CustomLoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        request.session['username'] = user.username  # Lưu tên người dùng vào session
        messages.success(request, 'Đăng nhập thành công!')
        return Response({"message": "Logged in successfully"}, status=200)
    
#Changed pasword
class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('password_change_done')
    def form_valid(self, form): 
        messages.success(self.request, 'Thay đổi mật khẩu thành công!') 
        return super().form_valid(form)
    
#Quan li thong tin tai khoan
class UserDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self): 
        return self.request.user 
    def put(self, request, *args, **kwargs): 
        response = super().put(request, *args, **kwargs) 
        messages.success(request, 'Thông tin cá nhân đã được cập nhật thành công!') 
        return response 
    def patch(self, request, *args, **kwargs): 
        response = super().patch(request, *args, **kwargs) 
        messages.success(request, 'Thông tin cá nhân đã được cập nhật thành công!') 
        return response
