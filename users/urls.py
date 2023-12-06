from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
]
