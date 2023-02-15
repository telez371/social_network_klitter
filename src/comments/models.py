from django.db import models


class AbstractComments(models.Model):
    """Модель комментариев"""
    text = models.TextField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'Post by {self.text}'

    class Meta:
        abstract = True
