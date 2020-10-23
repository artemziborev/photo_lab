from django.contrib.auth import get_user_model
from django.db import models
from model_utils.models import TimeStampedModel


User = get_user_model()


class Event(models.Model):
    name = models.CharField('Название мероприятия', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

class Tag(models.Model):
    name = models.CharField('Название тэга', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Теги'



class Photo(TimeStampedModel):
    name = models.CharField('Название фото', max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos',
                             verbose_name='Загруженно пользователем :')
    file = models.ImageField(upload_to='photos', verbose_name='Файл изображения')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Мероприятие')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Comment(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария', related_name='comments')
    content = models.TextField('Содержание комментария')
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='comments',
                              verbose_name='Изображение')

    def __str__(self):
        return f'Комментарий пользователя {self.user} к изображению {self.photo.name}'