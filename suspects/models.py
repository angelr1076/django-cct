from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Suspect(models.Model):
    reported_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mugshot = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    description = models.TextField(blank=True)
    in_custody = models.BooleanField(default=False)
    spotted = models.ManyToManyField(User, blank=True, related_name="spot_suspect")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
        
    def serialize(self):
        return {
            'id': self.id,
            'user': self.reported_by,
            'user_id': self.reported_by.id,
            'reported_by ': self.reported_by,
            'description': self.description,
            'spotted': self.times_spotted(),
            'spot': [user.username for user in self.spotted.all()],
        }
        
    def times_spotted(self):
        return self.spotted.count()