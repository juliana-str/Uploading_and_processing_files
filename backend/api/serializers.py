from rest_framework import serializers

from .models import File

FORMATS = ['txt', 'csv', 'xlsx', 'yml']


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

    def validate_file(self, file):
        if file.content_type in FORMATS:
            return file
        raise TypeError(
            'Неверный формат файла! '
            'Загрузить можно файлы с расширением txt, csv, xlsx, yml'
        )
