from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import ModifiedUserCreationForm

# Create your views here.

def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('datasets')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request,'Username or password is wrong')

    return render(request, 'users/login-and-register.html')

def logoutUser(request):
    logout(request)
    messages.info(request, 'User was successfully logged out')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = ModifiedUserCreationForm()

    if request.method == 'POST':
        form = ModifiedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created')

            login(request, user)
            return redirect('datasets')
        
        else:
            messages.error(request, 'Could not process account creation')
    

    context = {'page': page, 'form': form}
    return render(request, 'users/login-and-register.html', context)

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(id_num=pk)

    skillsWithDesc = profile.skill_set.exclude(description__exact="")
    skillsWithoutDesc = profile.skill_set.filter(description="")

    context = {'profile':profile, 'skillsWithDesc': skillsWithDesc, 'skillsWithoutDesc': skillsWithoutDesc}
    return render(request, 'users/user-profile.html', context)
