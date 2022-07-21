from .views import *
from django.urls import path

urlpatterns = [
    path('register/', registerView, name="register"),
]