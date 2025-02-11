from django.shortcuts import render
from rubka.models import Series, Episode
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rubka.models import Comment
from .serializers import CommentSerializer, SeriesSerializer, EpisodeSerializer


def get_api_documentation(request):
    return render(request, 'api_documentation.html')


@api_view(['GET'])
def get_series(request, simple_url):
    try:
        series = Series.objects.get(simple_url=simple_url)
    except Series.DoesNotExist:
        return Response({'error': 'Series.DoesNotExist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SeriesSerializer(series)
        return Response(serializer.data)
    
    
@api_view(['GET'])
def get_all_series_episodes(request, simple_url):
    try:
        series = Series.objects.get(simple_url=simple_url)
        episodes_list = series.episodes.order_by('episode_number')
    except Series.DoesNotExist:
        return Response({'error': 'Сериал не найден'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EpisodeSerializer(episodes_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
    
@api_view(['GET'])
def episodes_list(request):
    series_id = request.GET.get('series')  # Получаем ID сериала из запроса

    if series_id:
        episodes = Episode.objects.filter(series_id=series_id)  # Фильтр по сериалу
    else:
        episodes = Episode.objects.all()  # Все серии

    serializer = EpisodeSerializer(episodes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def episode_detail(request, pk):
    try:
        episode = Episode.objects.get(pk=pk)
        serializer = EpisodeSerializer(episode)
        return Response(serializer.data)
    except Episode.DoesNotExist:
        return Response({'error': 'Эпизод не найден'}, status=status.HTTP_404_NOT_FOUND)



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])  # Авторизация не нужна для просмотра, но нужна для добавления
def comment_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Указываем автором текущего пользователя
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comment_detail(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response({'error': 'Комментарий не найден'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        if comment.user != request.user:  # Только автор может редактировать
            return Response({'error': 'Вы не можете редактировать этот комментарий'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if comment.user != request.user:  # Только автор может удалять
            return Response({'error': 'Вы не можете удалить этот комментарий'}, status=status.HTTP_403_FORBIDDEN)

        comment.delete()
        return Response({'message': 'Комментарий удален'}, status=status.HTTP_204_NO_CONTENT)
