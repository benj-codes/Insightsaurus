from django.shortcuts import render
from django.http import HttpResponse
from .models import Dataset

# Create your views here.
def datasets(request):
    datasets = Dataset.objects.all()
    context = {'datasets': datasets}
    return render(request, 'datasets/datasets.html', context)

def dataset(request, pk):
    datasetObj = Dataset.objects.get(id_num=pk)
    return render(request, 'datasets/single-dataset.html', {'dataset':datasetObj})