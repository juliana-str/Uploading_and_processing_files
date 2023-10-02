from rest_framework import serializers

from .models import File


class FileSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели файлов, просмотр, загрузка."""

    class Meta:
        fields = ('file', 'uploaded_at', 'processed')
        model = File
