from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class CustomUser(AbstractUser):
    # Add any additional fields you want to the user model here
    is_banned = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('profile')
    def __str__(self):
        return self.username