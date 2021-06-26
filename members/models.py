from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})

    def serialize(self):
        return {
            'id': self.id,
            'bio': self.bio,
        }
