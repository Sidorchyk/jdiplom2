from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import User

class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class MyLoginView(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('main:index')

class MyLogoutView(LogoutView):
    next_page = reverse_lazy('main:index')

