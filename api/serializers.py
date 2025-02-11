from rest_framework import serializers
from rubka.models import Series, Comment, Episode


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = '__all__'  # Можно перечислить только нужные поля, например: ['id', 'name', 'genre']
        
        
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  # Чтобы не передавать user вручную
    class Meta:
        model = Comment
        fields = ['id', 'series', 'user', 'text', 'created_at']
        
        
class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = '__all__'
