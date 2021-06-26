from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Profile
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm
from .forms import ProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from django.views import generic
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User

# All officers view
def officers(request):
    officers = User.objects.order_by('-last_name').filter(is_staff=True)
    paginator = Paginator(officers, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'officers': officers,
        'page_obj': page_obj,
    }
    
    return render(request, 'registration/officers.html', context)
    
    
# Auth functions
def register(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Passwords do not match')
                return redirect('register')
            else: 
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username, password=password1, first_name=first_name, last_name=last_name, email=email
                        )
                    user.save()
                    login(request, user)
                    messages.success(request, 'Registered successfully')
                    print('registered successfully')
                    return redirect('home')
        else:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'registration/register.html', {'form': form})
    
    else:
        return render(request, 'registration/register.html', {'form': form})


def loginuser(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request, username=username, password=password)

        if user is None:
            messages.error(
                request, 'Username is not valid, or you entered the wrong password')
            return render(request, 'registration/loginuser.html', {'form': form})

        else:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('home')
    else:
        return render(request, 'registration/loginuser.html', {'form': form})
        

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, 'Logged out successfully')
        return redirect('loginuser')


class CreateProfileView(SuccessMessageMixin,CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile.html'
    success_url = reverse_lazy('home')
    success_message = 'Profile was created successfully'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfileView(SuccessMessageMixin, UpdateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/edit_profile.html'

    success_message = "Profile updated."
    success_url = reverse_lazy('home')
    success_message = 'Profile was edited successfully'


class ProfileView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context
