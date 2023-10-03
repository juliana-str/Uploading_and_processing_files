from django.db import transaction
from rest_framework import serializers

from .models import File


class FileSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели файлов, просмотр, загрузка."""
    processed = serializers.SerializerMethodField()

    class Meta:
        fields = ('file', 'uploaded_at', 'processed')
        model = File

    def get_processed(self, obj):
        return File.objects.filter(obj=obj).exists()

    @transaction.atomic
    def create(self, validated_data):
        file = File.objects.create(**validated_data)

        return file
