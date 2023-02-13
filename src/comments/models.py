from django.db import models


class AbstractComments(models.Model):
    """Модель комментариев"""
    text = models.TextField('Сообщение', max_length=500)
    created_date = models.DateTimeField('Дата добавления', auto_now_add=True)
    update_date = models.DateTimeField('Изменен', auto_now=True)
    published = models.BooleanField('Опубликовать?', default=True)
    deleted = models.BooleanField('Удалить?', default=False)

    def __str__(self):
        return f'Post by {self.text}'

    class Meta:
        abstract = True
