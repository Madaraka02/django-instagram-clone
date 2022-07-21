from .views import *
from django.urls import path
from users.views import *

urlpatterns = [
    path('', home, name="home"),
    path('profile/<int:id>/', userProfile, name="profile"),
    path('profile/<int:id>/follow/', follow, name="follow"),
    path('profile/<int:id>/unfollow/', unfollow, name="unfollow"),

]