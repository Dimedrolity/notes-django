from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.TextField(verbose_name="Заголовок", default='', blank=True)
    text = models.TextField(verbose_name="Основной текст", default='', blank=True)

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return self.title