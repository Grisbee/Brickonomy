from django.urls import path
from . import views
from .views import MifigurePostList, MinifigureCreateView

urlpatterns = [
    path('minifigures/', views.MifigurePostList.as_view(), name="minifigures-page"),
    path('minifigure_post/<int:pk>/', views.MinifigureDetailView.as_view(), name="minifigures-post"),
    path('minifigure_post/new/', views.MinifigureCreateView.as_view(), name="minifigures-create"),
    path('sets', views.sets, name="sets-page"),
    path('', views.home, name="home-page"),
    path('explore', views.explore, name="explore-page")
]