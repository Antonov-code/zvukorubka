from rubka.models import Series


def get_all_series_list (request):
    return {"all_series" : Series.objects.all()[:20]}

def get_anime_list (request):
    return {"all_anime": Series.objects.filter(type='anime')[:20]}

def get_podcast_list (request):
    return {"all_podcast": Series.objects.filter(type='podcast')[:20]}

# def get_serials_list (request):
#     return {"all_serials": Series.objects.filter(type='serials')}