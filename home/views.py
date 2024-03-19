from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Set, User
from django.urls import reverse_lazy
from .models import Minifigure
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Sum


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
    context_object_name = 'minifigure_list'
    ordering = 'date_added'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_minifigures_count = Minifigure.objects.filter(owner_name=self.request.user.username).count()
        user_minifigures_value = Minifigure.objects.filter(owner_name=self.request.user.username).aggregate(total_value=Sum('estimated_price'))

        context['user_minifigures_count'] = user_minifigures_count
        context['user_minifigures_value'] = user_minifigures_value.get('total_value')
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


class MinifigureUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Minifigure
    fields = ['character_name', 'if_custom', 'era', 'description', 'estimated_price',
              'quantity', 'date_added']
    login_url = reverse_lazy('login')
    template_name = 'home/minifigure_update.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.owner:
            return True
        return False


def explore(request):
    return render(request, "home/explore.html")


class ExploreMinifigures(ListView):
    model = Minifigure
    template_name = 'home/explore_minifigures.html'
    context_object_name = 'minifigure_post'
    ordering = 'date_added'

