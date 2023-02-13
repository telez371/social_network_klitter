from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from src.wall.models import Post, Comment


@admin.register(Post)
class CommentAdmin(admin.ModelAdmin):
    """Модель постов"""
    list_display = ("user", "view_count", "create_date", "moderation", "published", "id")

@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    """Комментарий к постам"""
    list_display = ("user", "post", "created_date", "update_date", "published", "id")
    # actions = ['unpublish', 'publish']
    mptt_level_indent = 15