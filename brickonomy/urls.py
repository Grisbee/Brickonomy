"""
URL configuration for brickonomy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from home import views
from users import views as users_views
from django.conf import settings
from django.conf.urls.static import static
from users.views import ProfileView


urlpatterns = [
    path('brickonomy/admin/', admin.site.urls),
    path('brickonomy/register/', users_views.register, name='register'),
    path('brickonomy/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('brickonomy/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('brickonomy/profile', users_views.profile, name='profile'),
    path('brickonomy/profile/<int:pk>/', users_views.ProfileView.as_view(), name='view_profile'),
    path('brickonomy/view_profile/<int:pk>/', users_views.ProfileView.as_view(), name='view_other_profile'),
    path('brickonomy/', include("home.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
