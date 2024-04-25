from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Profile, Message, Skill
from .forms import ModifiedUserCreationForm, ProfileForm, SkillForm, MessageForm

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
            return redirect('datasets')
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
            return redirect('edit-account')
        
        else:
            messages.error(request, 'Could not process account creation')
    

    context = {'page': page, 'form': form}
    return render(request, 'users/login-and-register.html', context)

def profiles(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        print('SEARCH:', search_query)
    
    skills = Skill.objects.filter(name__icontains=search_query)

    profiles = Profile.objects.distinct().filter(Q(name__icontains=search_query) | Q(skill__in=skills))
    context = {'profiles': profiles, 'search_query': search_query}
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(id_num=pk)

    skillsWithDesc = profile.skill_set.exclude(description__exact="")
    skillsWithoutDesc = profile.skill_set.filter(description="")

    context = {'profile':profile, 'skillsWithDesc': skillsWithDesc, 'skillsWithoutDesc': skillsWithoutDesc}
    return render(request, 'users/user-profile.html', context)

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    context = {'profile': profile, 'skills': skills}
    return render(request, 'users/account.html', context)

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid:
            form.save()

            return redirect('account')

    context = {'form': form}
    return render(request, 'users/profile_form.html', context)

@login_required(login_url='login')
def addSkill(request):
    profile = request.user.profile
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request,'Awesome! You added a new skill!')
            return redirect('account')
    context = {'form': form}
    return render (request, 'users/account-skills.html', context)

@login_required(login_url='login')
def updateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id_num=pk)
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            
            form.save()
            messages.success(request,'Hey! You updated a skill!')
            return redirect('account')
    context = {'form': form}
    return render (request, 'users/account-skills.html', context)

def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id_num=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request,'Skill has been removed!')
        return redirect('account')
    context = {'object': skill}
    return render(request, 'users/delete-account-skills.html', context)

@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    messageReqs = profile.messages.all()
    unreadCount = messageReqs.filter(is_read=False).count()
    context = {'messageReqs': messageReqs, 'unreadCount': unreadCount}
    return render(request, 'users/inbox.html', context)

@login_required(login_url='login')
def readMessage(request, pk):
    profile = request.user.profile
    message = profile.messages.get(id_num=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()
    context = {'message': message}
    return render(request, 'users/message.html', context)


def createMessage(request, pk):
    recipient = Profile.objects.get(id_num=pk)
    form = MessageForm()
    try:
        sender = request.user.profile
    except:
        sender = None
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()

            messages.success(request, 'Your message was sent!')
            return redirect('user-profile', pk=recipient.id_num)

    context = {'recipient': recipient, 'form': form}
    return render(request, 'users/message-form.html', context)

