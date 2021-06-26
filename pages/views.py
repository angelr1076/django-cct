from django.shortcuts import render
from crimes.models import Crime
from crimes.forms import NewCrimeForm, UpdateCrimeForm
from suspects.models import  Suspect


def home(request):
    crimes = Crime.objects.order_by('-crime_date').filter(is_active=True)
    suspects = Suspect.objects.all()
    form = NewCrimeForm()
    
    context = {
        'crimes': crimes,
        'suspects': suspects,
        'form': form
    }
    
    return render(request, 'pages/home.html', context)
