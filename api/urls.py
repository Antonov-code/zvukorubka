from django.urls import path
from api.views import get_api_documentation, episodes_list, episode_detail, get_all_series_episodes
from .views import get_series, comment_list, comment_detail


# /api/...
urlpatterns = [
    path('', get_api_documentation),
    path('series/<str:simple_url>/', get_series, name='get_series'),
    path('series/all_episodes/<str:simple_url>/', get_all_series_episodes, name='get_all_series_episodes'),
    path('episodes/', episodes_list, name='episodes_list'),
    path('episodes/<int:pk>/', episode_detail, name='episode_detail'),
    
    path('comments/', comment_list, name='comment_list'),  # Список и добавление комментариев
    path('comments/<int:pk>/', comment_detail, name='comment_detail'),  # Просмотр, изменение, удаление
]