from django.urls import path
from . import views

urlpatterns = [
    path('minifigures', views.minifigures, name="minifigures-page"),
    path('sets', views.sets, name="sets-page"),
    path('', views.home, name="home-page"),
    path('explore', views.explore, name="explore-page")
]