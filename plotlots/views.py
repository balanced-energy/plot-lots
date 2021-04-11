from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'plotlots/index.html', context)