from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from rubka.models import Series, BannerOnTheMainPage, VoiceActor


def main_page(request, format=None):
    banners = BannerOnTheMainPage.objects.filter(is_active='True')
    return render(request, 'index.html', context={'banners' : banners})


def watch_page(request, simple_url):
    try:
        series = Series.objects.get(simple_url=simple_url)
        if series:
            voice_actors = series.voice_actors.all()
            genres = series.genre.all()
            episodes = series.episodes.order_by('episode_number')
            banners = series.banners.all()
            studios = series.studio.all()
            return render(request, 'watch.html', context={'series' : series, 'episodes' : episodes, 'voice_actors' : voice_actors, 'genres' : genres, 'banners' : banners, 'studios' : studios})
    except:
        return render(request, '404.html')


def anime_page(request, format=None):
    all_series = Series.objects.filter(type='anime').prefetch_related('genre', 'studio').order_by('-id')[:20]
    return render(request, 'anime_list.html', context={'all_series' : all_series})


def serial_page(request, format=None):
    all_series = Series.objects.filter(type='serials').prefetch_related('genre', 'studio').order_by('-id')[:20]
    return render(request, 'serial_list.html', context={'all_series' : all_series})


def popular_page(request, format=None):
    all_series = Series.objects.all().prefetch_related('genre', 'studio').order_by('-id')[:20]
    return render(request, 'popular_list.html', context={'all_series' : all_series})


def about_page(request, format=None):
    all_voice_actor = VoiceActor.objects.all()
    return render(request, 'about.html', context={'all_voice_actor' : all_voice_actor})


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        nickname = request.POST.get('nickname')

        if nickname:
            if password != password2:
                return render(request, 'login.html', {'error': 'Пароли должны совпадать!'})
            if CustomUser.objects.filter(email=email).exists():
                return render(request, 'login.html', {'error': 'Пользователь уже существует'})

            user = CustomUser.objects.create_user(email=email, password=password, username=nickname, nickname=nickname)
            auth_login(request, user)
            return redirect('/')
        else:
            user = authenticate(request, username=email, password=password)
            if user:
                auth_login(request, user)
                return redirect('/')
            else: # костыль по причине того что authenticate() не работает, а на разбор причины почему уже ушло слишком много времени, поэтому вручную сравниваем хеш с введённым паролем
                try:
                    user = CustomUser.objects.get(email=email)
                    if check_password(password, user.password):
                        auth_login(request, user)
                        return redirect('/')
                    return render(request, 'login.html', {'error': 'Неверные логин или пароль'})
                except:
                    return render(request, 'login.html', {'error': 'Неверные логин или пароль'})

    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('/login')


def profile_page(request, format=None):
    return render(request, 'profile.html')


def privacy_policy(request):
    return render(request, 'forms/privacy_policy.html')

