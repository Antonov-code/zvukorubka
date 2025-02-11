from django.contrib import admin
from rubka.models import Series, Episode, Genre, VoiceActor, Studio, BannerOnTheMainPage, Banner, CustomUser, Comment

admin.site.register(Series)
admin.site.register(Episode)
admin.site.register(Genre)
admin.site.register(VoiceActor)
admin.site.register(Comment)
admin.site.register(Studio)
admin.site.register(BannerOnTheMainPage)
admin.site.register(Banner)
admin.site.register(CustomUser)