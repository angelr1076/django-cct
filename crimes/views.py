import json
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from .models import Crime
from suspects.models import Suspect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import NewCrimeForm, UpdateCrimeForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import permission_required
from django.contrib import messages


def crimes(request):
    crimes = Crime.objects.order_by('-crime_date').filter(solved=False)
    paginator = Paginator(crimes, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    suspects = Suspect.objects.all()
    form = NewCrimeForm()
    
    context = {
        'crimes': crimes,
        'page_obj': page_obj,
        'suspects': suspects,
        'form': form,
    }
    
    return render(request, 'crimes/crimes.html', context)
    
def solved_crimes(request):
    crimes = Crime.objects.order_by('-crime_date').filter(solved=True)
    paginator = Paginator(crimes, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    suspects = Suspect.objects.all()
    form = NewCrimeForm()
    
    context = {
        'crimes': crimes,
        'page_obj': page_obj,
        'suspects': suspects,
        'form': form,
    }
    
    return render(request, 'crimes/solvedcrimes.html', context)
    
    
def crime(request, crime_id):
    crime = get_object_or_404(Crime, pk=crime_id)
    
    context = {
        'crime': crime,
    }
    
    return render(request, 'crimes/crime.html', context)


def usercrimelist(request):
    user = request.user
    crimes = Crime.objects.order_by('-crime_date').filter(reported_by=user)
    paginator = Paginator(crimes, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    form = NewCrimeForm()
    
    context = {
        'crimes': crimes,
        'page_obj': page_obj,
        'form': form,
    }
    
    return render(request, 'crimes/crimelist.html', context)
    

def report(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            reported_by = request.user
        else:
            reported_by = None
            
        crime_type = request.POST['crime_type']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        photo = request.FILES.get('photo_main')
        description = request.POST['description']
        suspect = request.POST.get('suspect')
        
        if suspect == "Not Seen":
            crime = Crime(crime_type=crime_type, address=address, city=city, state=state, photo_main=photo, reported_by=reported_by, description=description)
        else:
            print("suspect reported")
            crime = Crime(crime_type=crime_type, address=address, city=city, state=state,  photo_main=photo, reported_by=reported_by, description=description, suspect_id=suspect)
        
        crime.save()
        messages.success(request, 'Crime reported successfully')
        return redirect('/crimes')
        
def editcrime(request, crime_id):
    crime = get_object_or_404(Crime, id=crime_id)
    
    if request.method == 'GET':
        form = UpdateCrimeForm(instance=crime)
        
        context = {
            'crime': crime,
            'form': form,
        }
        
        return render(request, 'crimes/editcrime.html', context)
    
    else:
        try:
            form = UpdateCrimeForm(request.POST, request.FILES, instance=crime)
            if form.is_valid():
                form.save()
                messages.success(request, 'Crime edited successfully')
                return HttpResponseRedirect(reverse('crimes'))
        except ValueError:
            messages.error(request, 'An error occured')
            return render(request, 'crimes/editcrime.html', context)
            
    if request.method == 'PUT':
        data = json.loads(request.body)
        description = data.get('description', '')
        Crime.objects.filter(pk=crime_id).update(description=description)
        messages.success(request, 'Crime edited successfully')
        return JsonResponse({'message': 'Crime updated'}, status=201)
           
            