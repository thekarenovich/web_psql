from django.utils import timezone
from django.db import models


class Articles(models.Model):
    # category = models.CharField('Категория', max_length=35)
    title = models.CharField(max_length=50, verbose_name='Название')
    anons = models.CharField(max_length=250, verbose_name='Анонс')
    full_text = models.TextField(verbose_name='Статья')
    # photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    date = models.DateTimeField(null=True, blank=True, default=timezone.now(), verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
