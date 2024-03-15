from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
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


class MifigurePostList(ListView):
    model = Minifigure
    template_name = 'home/minifigures.html'
    context_object_name = 'minifigure_post'
    ordering = 'date_added'


class MinifigureDetailView(DetailView):
    model = Minifigure
    template_name = 'home/minifigure_post.html'


class MinifigureCreateView(CreateView):
    model = Minifigure
    fields = ['character_name', 'if_custom', 'era', 'description', 'estimated_price',
              'quantity', 'date_added', 'owner']


def explore(request):
    return render(request, "home/explore_page.html")
