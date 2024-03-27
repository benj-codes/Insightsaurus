from django.shortcuts import render
from django.http import HttpResponse

datasetsList = [
    {
        'id': '1',
        'title': 'Japan Birth Demographics',
        'description': 'Data analysis applied to Japan Birth Demographics dataset.'
    },
    {
        'id': '2',
        'title': 'Crime Statistics Calgary',
        'description': 'Data analysis applied to Crime Statistics Calgary dataset.'
    },
    {
        'id': '3',
        'title': 'Video game sales',
        'description': 'Data analysis applied to Video Game Sales dataset.'
    },
]

# Create your views here.
def datasets(request):
    page = 'Datasets'
    number = 10
    context = {'page': page, 'number':number, 'datasets': datasetsList}
    return render(request, 'datasets/datasets.html', context)

def dataset(request, pk):
    datasetObj = None
    for i in datasetsList:
        if i['id'] == pk:
            datasetObj = i
    return render(request, 'datasets/single-dataset.html', {'dataset':datasetObj})