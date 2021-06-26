from django.shortcuts import render
from .models import Crime

def crime_count(request):
    crimes = Crime.objects.all().filter(is_active=True)
    crime_total = len(crimes)
    
    return { 'crime_total': crime_total }
