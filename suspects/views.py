import json
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from .models import Suspect
from django.contrib.auth.models import User
from crimes.models import Crime
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import NewSuspectForm, SuspectEditForm
import jsonpickle
from json import JSONEncoder
from django.contrib import messages


def suspects(request):
    suspects = Suspect.objects.order_by('-last_name').filter(in_custody=False)
    paginator = Paginator(suspects, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    form = NewSuspectForm()
    
    context = {
        'suspects': suspects,
        'page_obj': page_obj,
        'form': form,
    }
    
    return render(request, 'suspects/suspects.html', context)
    

def nabbed_suspects(request):
    suspects = Suspect.objects.order_by('-last_name').filter(in_custody=True)
    paginator = Paginator(suspects, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    form = NewSuspectForm()
    
    context = {
        'suspects': suspects,
        'page_obj': page_obj,
        'form': form,
    }
    
    return render(request, 'suspects/nabbedsuspects.html', context)
    
    
def suspect(request, suspect_id):
    suspect = get_object_or_404(Suspect, pk=suspect_id)
    crimes = Crime.objects.all().filter(suspect=suspect)
    
    context = {
        'suspect': suspect,
        'crimes': crimes,
    }
    
    return render(request, 'suspects/suspect.html', context)
    
    
def usersuspectlist(request):
    user = request.user
    suspects = Suspect.objects.order_by('-last_name').filter(reported_by=user)
    paginator = Paginator(suspects, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    form = NewSuspectForm()
    
    context = {
        'suspects': suspects,
        'page_obj': page_obj,
        'form': form,
    }
    
    return render(request, 'suspects/suspectlist.html', context)
    
def createsuspect(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            reported_by = request.user
        else:
            reported_by = None
            
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        photo = request.FILES.get('mugshot')
        description = request.POST['description']
        in_custody = request.POST.get('in_custody')
        
        if in_custody is None:
            suspect = Suspect(first_name=first_name, last_name=last_name, mugshot=photo, description=description, reported_by=reported_by, in_custody=False)
        else:
            suspect = Suspect(first_name=first_name, last_name=last_name, mugshot=photo, description=description, reported_by=reported_by, in_custody=True)
        
        suspect.save()
        messages.success(request, 'Suspect reported successfully')
        return redirect('/suspects')
        
    
def editsuspect(request, suspect_id):
    suspect = get_object_or_404(Suspect, id=suspect_id)
    
    if request.method == 'GET':
        form = SuspectEditForm(instance=suspect)
        
        context = {
            'suspect': suspect,
            'form': form,
        }
        
        return render(request, 'suspects/editsuspect.html', context)
    
    else:
        try:
            form = SuspectEditForm(request.POST, request.FILES, instance=suspect)
            if form.is_valid():
                form.save()
                messages.success(request, 'Suspect edited successfully')
                return HttpResponseRedirect(reverse('suspects'))
        except ValueError:
            messages.error(request, 'An error occured')
            return render(request, 'suspects/editsuspect.html', context)
            
    if request.method == 'PUT':
        data = json.loads(request.body)
        description = data.get('description', '')
        Suspect.objects.filter(pk=suspect_id).update(description=description)
        messages.success(request, 'Suspect edited successfully')
        return JsonResponse({'message': 'Suspect updated'}, status=201)
            

def spotted_view(request, suspect_id):
    try: 
        user = User.objects.get(username=request.user)
        suspect = Suspect.objects.get(pk=suspect_id)

    except Suspect.DoesNotExist:
        return JsonResponse({'error': 'Suspect does not exist'}, status=400)
        
    if request.method == 'GET':
        return JsonResponse(suspect.serialize())
    
    if request.method == 'PUT':
        spotted = False
        if suspect.spotted.filter(username=user).exists():
            suspect.spotted.remove(user)
            spotted = False
            spotJSON = jsonpickle.encode(suspect.serialize(), unpicklable=False)
            spotJSONData = json.dumps(spotJSON, indent=4)
            SuspectJSON = jsonpickle.decode(spotJSONData)
            susJSON = json.loads(SuspectJSON)
            return JsonResponse(susJSON)
        else:
            suspect.spotted.add(user)
            spotted = True
            spotJSON = jsonpickle.encode(suspect.serialize(), unpicklable=False)
            spotJSONData = json.dumps(spotJSON, indent=4)
            SuspectJSON = jsonpickle.decode(spotJSONData)
            susJSON = json.loads(SuspectJSON)
            return JsonResponse(susJSON)
    return JsonResponse({'message': 'Spotted status updated'}, status=201)
    
    