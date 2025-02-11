"""
URL configuration for zvukorubka project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from rubka.views import main_page, about_page, anime_page, serial_page, popular_page, watch_page, login, logout, profile_page, privacy_policy
import api.urls


urlpatterns = [
    path('', main_page, name='home'),
    path('admin/', admin.site.urls, name='admin'),
    path('watch/<str:simple_url>', watch_page, name='home'),
    path('anime/', anime_page, name='anime'),
    path('serials/', serial_page, name='serials'),
    path('popular/', popular_page, name='popular'),
    path('about/', about_page, name='about'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile_page, name='profile'),
    path('privacy_policy/', privacy_policy, name='privacy_policy'),

    path('api/', include('api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)