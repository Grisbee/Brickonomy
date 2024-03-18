from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Set, User
from django.urls import reverse_lazy
from .models import Minifigure
from django.contrib.auth.mixins import LoginRequiredMixin


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minifigure_amount'] = Minifigure.owner_name
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_minifigures_count = Minifigure.objects.filter(owner_name=self.request.user.username).count()
        context['user_minifigures_count'] = user_minifigures_count
        return context


class MinifigureDetailView(DetailView):
    model = Minifigure
    template_name = 'home/minifigure_post.html'


class MinifigureCreateView(LoginRequiredMixin, CreateView):
    model = Minifigure
    fields = ['character_name', 'if_custom', 'era', 'description', 'estimated_price',
              'quantity', 'date_added']
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MinifigureUpdateView(LoginRequiredMixin, UpdateView):
    model = Minifigure
    fields = ['character_name', 'if_custom', 'era', 'description', 'estimated_price',
              'quantity', 'date_added']
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


def explore(request):
    return render(request, "home/explore.html")


class ExploreMinifigures(ListView):
    model = Minifigure
    template_name = 'home/explore_minifigures.html'
    context_object_name = 'minifigure_post'
    ordering = 'date_added'

