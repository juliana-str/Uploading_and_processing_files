import logging

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

    def validate_file(self, file):
        if file.content_type != 'text/plain':
            raise TypeError(
                'Неверный формат файла! '
                'Загрузить можно файл с расширением txt'
            )
        if file.size == 0:
            raise TypeError('Файл не должен быть пустым')

        return file
