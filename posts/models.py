from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300,blank=True)
    image = models.FileField(upload_to="posts/images", blank=True)
    caption = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')

    def __str__(self):
        return self.title


