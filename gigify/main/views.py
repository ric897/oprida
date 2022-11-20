from django.shortcuts import render

# Create your views here.


def index(request):
    context = {}
    return render(request, 'index.html', context)

def approach(request):
    context = {}
    return render(request, 'approach.html', context)

def startups(request):
    context = {}
    return render(request, 'startups.html', context)

def enterprises(request):
    context = {}
    return render(request, 'enterprise.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)
