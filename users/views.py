from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.

def loginUser(request):

    if request.user.is_authenticated:
        return redirect('datasets')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print('Username does not exist')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            print('Username or password is wrong')

    return render(request, 'users/login-and-register.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

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
