from django.db import models
from datetime import datetime
from suspects.models import Suspect
from django.contrib.auth.models import User
from crimes.choices import CRIME_CHOICES, STATE_CHOICES

   
class Crime(models.Model):
    reported_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    suspect = models.ForeignKey(Suspect, null=True, blank=True, on_delete=models.DO_NOTHING)
    crime_type = models.CharField(choices=CRIME_CHOICES, max_length=200, default='NA')
    address = models.CharField(max_length=200)
    city = models.CharField(null=True, blank=True, max_length=100)
    state = models.CharField(choices=STATE_CHOICES, null=True, blank=True, max_length=100, default='NA')
    zipcode = models.CharField(null=True, blank=True,max_length=20)
    description = models.TextField(null=True, blank=True)
    photo_main = models.ImageField(null=True, blank=True, upload_to='photos/%Y/%m/%d/')
    is_active = models.BooleanField(default=True)
    crime_date = models.DateTimeField(default=datetime.now, blank=True)
    solved = models.BooleanField(default=False)

    def __str__(self):
        return self.crime_type
        
    def serialize(self):
        return {
            'id': self.id,
            'reported_by': self.reported_by,
            'description': self.description,
        }