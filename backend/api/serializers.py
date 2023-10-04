from django.db import transaction
from rest_framework import serializers

from .models import File


class FileListSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели файлов, просмотр списка файлов."""
    processed = serializers.BooleanField()

    class Meta:
        fields = ('id', 'file', 'uploaded_at', 'processed')
        model = File


class FilePostSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели файлов, загрузка."""
    file = serializers.FileField()

    class Meta:
        fields = ('id', 'file', 'uploaded_at')
        model = File
