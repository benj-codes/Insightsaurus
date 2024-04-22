from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Dataset, Review, Japan, FoodWaste
from .forms import ReviewForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.mixins import LoginRequiredMixin

#@login_required(Login_url="login")

# Create your views here.
def datasets(request):
    datasets = Dataset.objects.all()
    context = {'datasets': datasets}
    return render(request, 'datasets/datasets.html', context)

def dataset(request, pk):
    datasetObj = Dataset.objects.get(id_num=pk)
    has_reviewed = user_has_reviewed(request.user, datasetObj)
    form = ReviewForm()
    # chart_data = None
    japan_data = None
    food_data = None

    dataset_name = datasetObj.title

    if dataset_name == 'Japan Birth Demographics':
        japan_data = Japan.objects.all()
    #    chart_data = japan_data
    elif dataset_name == 'Food Waste':
        food_data = FoodWaste.objects.all()
    #    chart_data = food_data
       

    # Allow user to comment view
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.dataset = datasetObj
        review.owner = request.user.profile
        review.save()

        #Allow vote cast view
        datasetObj.getVoteCount

        messages.success(request, 'Feedback successfully added!')
        return redirect('dataset', pk=datasetObj.id_num)


    return render(request, 'datasets/single-dataset.html', {'dataset':datasetObj, 'form':form, 'has_reviewed': has_reviewed, 'japan_data': japan_data, 'food_data': food_data})

# Check if user has reviewed dataset
def user_has_reviewed(user, dataset):
    # Check user is logged in
    if isinstance(user, AnonymousUser) or not user.is_authenticated:
        return False, None
    # Get the review with user and dataset if it exists
    print(f"User: {user.profile} Data: {dataset.id_num}")
    review = Review.objects.filter(owner=user.profile, dataset=dataset.id_num).first()
    if review:
     return True
    else:
     return None
    
