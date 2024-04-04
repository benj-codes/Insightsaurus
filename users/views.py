from django.shortcuts import render
from .models import Profile

# Create your views here.

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
