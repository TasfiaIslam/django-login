from django.urls import path
from .views import UserCreate

urlpatterns = [
    path('register/', UserCreate.as_view(), name='create_user'),
]
