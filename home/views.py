from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Set, User
from django.urls import reverse_lazy
from .models import Minifigure, Gallery
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Sum
import os


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        images = Gallery.objects.filter(minifigure=self.get_object())
        context['images'] = images
        return context


class MinifigureCreateView(LoginRequiredMixin, CreateView):
    model = Minifigure
    fields = ['character_name', 'if_custom', 'era', 'description', 'estimated_price',
              'quantity', 'date_added', 'image']
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MinifigureUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Minifigure
    fields = ['character_name', 'if_custom', 'era', 'description', 'estimated_price',
              'quantity', 'date_added', 'image']
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


class MinifigureDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Minifigure
    template_name = 'home/minifigure_delete.html'
    success_url = '/brickonomy/minifigures/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.owner:
            return True
        return False


class ExploreMinifigures(ListView):
    model = Minifigure
    template_name = 'home/explore_minifigures.html'
    context_object_name = 'minifigures'


    def post(self, request):
        display_minifigures = request.POST['display_figures']
        filtering = request.POST['filters']
        ordering = '-date_added'

        if filtering == "most_expensive":
            ordering = '-estimated_price'
        elif filtering == "name":
            ordering = 'character_name'
        elif filtering == "least_expensive":
            ordering = 'estimated_price'
        elif filtering == "date_added":
            ordering = '-date_added'

        if display_minifigures == "all":
            minifigures = Minifigure.objects.all()
        elif display_minifigures == "custom":
            minifigures = Minifigure.objects.filter(if_custom=True)
        elif display_minifigures == "original":
            minifigures = Minifigure.objects.filter(if_custom=False)

        minifigures_ordered = minifigures.order_by(ordering)

        return render(request, "home/explore_minifigures.html", {"minifigures": minifigures_ordered})


class AddPhotos(LoginRequiredMixin, UserPassesTestMixin, View):
    model = Gallery

    def test_func(self):
        pk = self.kwargs.get('pk')
        fig = Minifigure.objects.filter(id=pk).first()
        if self.request.user == fig.owner:
            return True
        return False

    def get(self, request, pk):
        fig = Minifigure.objects.filter(id=pk).first()
        images = Gallery.objects.filter(minifigure=fig)
        #images = Gallery.objects.filter(id =pk)
        return render(request, "home/add_photos.html", {'images': images})

    def post(self, request, pk):
        images = request.FILES.getlist('images')
        fig = Minifigure.objects.filter(id=pk).first()

        for image in images:
            Gallery.objects.create(images=image, minifigure=fig)

        fig = Minifigure.objects.filter(id=pk).first()
        images = Gallery.objects.filter(minifigure=fig)
        return render(request, "home/add_photos.html", {'images': images})


class RemovePhotos(LoginRequiredMixin, UserPassesTestMixin, View):
    model = Gallery

    def test_func(self):
        pk = self.kwargs.get('pk')
        fig = Minifigure.objects.filter(id=pk).first()
        if self.request.user == fig.owner:
            return True
        return False

    def get(self, request, pk):
        fig = Minifigure.objects.filter(id=pk).first()
        images = Gallery.objects.filter(minifigure=fig)
        return render(request, "home/remove_photos.html", {'images': images})

    def post(self, request, pk):
        image_id = request.POST.get('image_id')

        image_to_delete = Gallery.objects.filter(id=image_id).first()
        image_path = image_to_delete.images.path
        image_to_delete.delete()
        os.remove(image_path)

        fig = Minifigure.objects.filter(id=pk).first()
        images = Gallery.objects.filter(minifigure=fig)

        return render(request, "home/remove_photos.html", {'images': images})

    #dodać żeby usuwało zdjęcia z galerii



