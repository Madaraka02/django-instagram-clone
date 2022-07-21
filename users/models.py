from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.FileField(upload_to='profile/images', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=300, null=True, blank=True)
    followers = models.ManyToManyField(User, blank=True, related_name='followers')

    def __str__(self):
        return self.user.username


 
 
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
  
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
        instance.profile.save()        