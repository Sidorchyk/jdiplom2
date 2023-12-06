from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('profile/<int:id>/', UserProfile.as_view(), name='profile'),
]

