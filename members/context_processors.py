from django.shortcuts import render
from .models import User

def officer_count(request):
    officers = User.objects.filter(is_staff=True)
    officer_total = len(officers)
    
    return { 'officer_total': officer_total }