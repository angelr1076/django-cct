from django.shortcuts import render
from .models import Suspect

def suspect_count(request):
    suspects = Suspect.objects.all()
    suspect_total = len(suspects)
    
    return { 'suspect_total': suspect_total }
