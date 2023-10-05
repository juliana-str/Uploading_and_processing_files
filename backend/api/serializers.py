from rest_framework import serializers

from .models import File


class FileListSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели файлов, просмотр списка файлов."""
    processed = serializers.BooleanField()

    class Meta:
        fields = '__all__'
        model = File


class FilePostSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели файлов, загрузка."""
    file = serializers.FileField()
    processed = serializers.BooleanField(default='False')

    class Meta:
        fields = '__all__'
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
