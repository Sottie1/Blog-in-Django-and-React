from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.utils.text import slugify
from shortuuid.django_fields import ShortUUIDField
import shortuuid

# Create your models here.

class User(AbstractUser):
    username = models.CharField(unique=True, max_length=200)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.username  # Ensure this returns a string

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        email_username, mobile = self.email.split('@')
        if not self.full_name:
            self.full_name = email_username

        if not self.username:
            self.username = email_username

        super(User, self).save(*args, **kwargs)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to="Profile Images", null=True, blank=True)
    full_name = models.CharField(max_length=200, null=True, blank=True)
    bio = models.CharField(max_length=100, null=True, blank=True)
    about = models.CharField(max_length=100, null=True, blank=True)
    author = models.BooleanField(default=False)
    country = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username  # Ensure this returns a string

    def save(self, *args, **kwargs):
        if not self.full_name:
            self.full_name = self.user.full_name

        super(Profile, self).save(*args, **kwargs)




def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance,  **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)