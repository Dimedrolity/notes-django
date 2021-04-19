from django.db import models


class Note(models.Model):
    title = models.TextField(verbose_name="Заголовок", default='', blank=True)
    text = models.TextField(verbose_name="Основной текст", default='', blank=True)
    date = models.DateTimeField(verbose_name="Дата и время", auto_now_add=True, null=True)


    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return self.title