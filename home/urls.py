from django.urls import path
from . import views
from .views import MifigurePostList, MinifigureCreateView, MinifigureUpdateView

urlpatterns = [
    path('', views.home, name="home-page"),

    path('explore/', views.explore, name="explore-page"),
    path('explore/explore_minifigures', views.ExploreMinifigures.as_view(), name="explore-minifigures"),

    path('minifigures/', views.MifigurePostList.as_view(), name="minifigures-page"),
    path('minifigure_post/new/', views.MinifigureCreateView.as_view(), name="minifigures-create"),
    path('minifigure_post/<int:pk>/', views.MinifigureDetailView.as_view(), name="minifigures-post"),
    path('minifigure_post/<int:pk>/update/', views.MinifigureUpdateView.as_view(), name="minifigures-update"),

    path('sets', views.sets, name="sets-page"),
]
