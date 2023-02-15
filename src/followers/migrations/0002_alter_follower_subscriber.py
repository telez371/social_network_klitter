# Generated by Django 4.1.6 on 2023-02-14 20:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('followers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='subscriber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriber', to=settings.AUTH_USER_MODEL),
        ),
    ]