from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Dataset
from .forms import ReviewForm
from django.contrib import messages

#@login_required(Login_url="login")

# Create your views here.
def datasets(request):
    datasets = Dataset.objects.all()
    context = {'datasets': datasets}
    return render(request, 'datasets/datasets.html', context)

def dataset(request, pk):
    datasetObj = Dataset.objects.get(id_num=pk)
    form = ReviewForm()
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

        


    return render(request, 'datasets/single-dataset.html', {'dataset':datasetObj, 'form':form})