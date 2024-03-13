from django.shortcuts import render
from django.http import HttpResponse
from .models import Set
from .models import Minifigure


def home(request):
    return render(request, 'home/home_page.html')


def minifigures(request):
    return render(request, 'home/minifigures.html')


def sets(request):
    context = {
        'sets': Set.objects.all()
    }
    return render(request, 'home/sets.html', context)


def explore(request):
    return render(request, "home/explore_page.html")