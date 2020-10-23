from rest_framework import serializers
from .models import Photo, Comment


class PhotoListSerializer(serializers.ModelSerializer):
    """
    Список фото
    """
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    class Meta:
        model = Photo
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):
    """
      Создание комментария
    """
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'



class PhotoDetailSerializer(serializers.ModelSerializer):
    """
    Детали фото
    """
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    comments = CommentCreateSerializer(many=True)
    class Meta:
        model = Photo
        fields = '__all__'


