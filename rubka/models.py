from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=20, blank=False)
    eng_name = models.CharField(max_length=20, blank=True, unique=True)

    def __str__(self):
        return self.name
    
    
class Episode(models.Model):
    EPISODE_NUMBER = [
        (1, '1 серия'),
        (2, '2 серия'),
        (3, '3 серия'),
        (4, '4 серия'),
        (5, '5 серия'),
        (6, '6 серия'),
        (7, '7 серия'),
        (8, '8 серия'),
        (9, '9 серия'),
        (10, '10 серия'),
        (11, '11 серия'),
        (12, '12 серия'),
        (13, '13 серия'),
        (14, '14 серия'),
        (15, '15 серия'),
        (16, '16 серия'),
        (17, '17 серия'),
        (18, '18 серия'),
        (19, '19 серия'),
        (20, '20 серия'),
        (21, '21 серия'),
        (22, '22 серия'),
        (23, '23 серия'),
        (24, '24 серия'),
    ]
    episode_number = models.IntegerField(blank=False, choices=EPISODE_NUMBER, default=1)
    name = models.CharField(max_length=100, blank=False)
    iframe = models.TextField(max_length=500, blank=False)

    def __str__(self):
        return f'{self.name}, {self.episode_number} серия'
    
    
class VoiceActor(models.Model):
    name = models.CharField(max_length=100, blank=False)
    bio = models.CharField(max_length=300, blank=True)
    eng_name = models.CharField(max_length=100, blank=False, unique=True)
    photo = models.ImageField(blank=True, upload_to='VoiceActors/')

    def __str__(self):
        return self.name


class Studio(models.Model):
    name = models.CharField(max_length=100, blank=False)
    eng_name = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField(max_length=600, blank=True)
    
    def __str__(self):
        return self.name


class BannerOnTheMainPage(models.Model):
    ACTIVES = [
        ('True', 'Активен'),
        ('False', 'Не активен'),
    ]
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=600, blank=True)
    prev_img = models.ImageField(blank=False, upload_to='prev_img/banners/', default='True')
    is_active = models.CharField(max_length=20, blank=False, choices=ACTIVES, default='True')
    
    def __str__(self):
        return self.title


class Banner(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=600, blank=True)
    prev_img = models.ImageField(blank=False, upload_to='prev_img/banners/', default='True')
    
    def __str__(self):
        return self.title


class Series(models.Model):
    AGES = [
        ('0', '0+'),
        ('12' , '12+'),
        ('14', '14+'),
        ('16' , '16+'),
        ('18' , '18+'),
    ]
    TYPES = [
        ('anime', 'Аниме'),
        ('podcast', 'Подкаст'),
        ('serials', 'Сериал'),
        ('film', 'Фильм'),
    ]

    simple_url = models.CharField(max_length=50, blank=False, unique=True)
    type = models.CharField(max_length=20, blank=False, choices=TYPES, default='anime')
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=600, blank=False)
    studio = models.ManyToManyField(Studio, blank=True)
    genre = models.ManyToManyField(Genre, blank=True)
    year_of_release = models.IntegerField(default=2025)
    age = models.CharField(max_length=3, choices=AGES, default='16')
    lasting = models.CharField(max_length=20, default='24 минуты')
    prev_img = models.ImageField(blank=False, upload_to='prev_img/', default='True')
    voice_actors = models.ManyToManyField(VoiceActor, blank=True)
    episodes = models.ManyToManyField(Episode, blank=True)
    banners = models.ManyToManyField(Banner, blank=True)
    
    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True
    )
    login = models.CharField(max_length=100, blank=True)
    nickname = models.CharField(max_length=100, blank=True)
    profile_img = models.ImageField(blank=True, upload_to='profile_images/')

    def __str__(self):
        return f'{self.nickname}'
    
    
class Comment(models.Model):
    series = models.ForeignKey('Series', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Комментарий от {self.user} к {self.series}"

