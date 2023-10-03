from django.db import models


class File(models.Model):
    file = models.FileField(
        db_index=True,
        upload_to='files/media',
        verbose_name='Файл'
    )
    uploaded_at = models.DateTimeField(
        verbose_name='Дата загрузки',
        auto_now_add=True
    )
    processed = models.BooleanField(
        verbose_name='Обработан'
    )

    class Meta:
        ordering = ['uploaded_at']
