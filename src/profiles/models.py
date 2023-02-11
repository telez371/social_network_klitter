from django.contrib.auth.models import AbstractUser
from django.db import models


class UserNet(AbstractUser):
    """Custom model"""
    GENDER = (
        ('--', '--'),
        ('male', 'male'),
        ('female', 'female')
    )

    middle_name = models.CharField(max_length=50)
    first_login = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='user/avatar', blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, default='--')

    def __str__(self):
        return self.middle_name


class Channel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    avatar = models.ImageField(upload_to='channel/avatars/', blank=True, null=True)
    creator = models.ForeignKey(UserNet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(UserNet, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Subscription(models.Model):
    user = models.ForeignKey(UserNet, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.middle_name} subscribed to {self.channel.name}'


class Reaction(models.Model):
    user = models.ForeignKey(UserNet, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    emoji = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.user.middle_name} reacted with {self.emoji} on {self.news}"


class Comment(models.Model):
    user = models.ForeignKey(UserNet, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.middle_name} commented on {self.news}"