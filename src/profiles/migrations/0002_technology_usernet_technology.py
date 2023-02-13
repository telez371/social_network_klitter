# Generated by Django 4.1.6 on 2023-02-13 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='usernet',
            name='technology',
            field=models.ManyToManyField(related_name='users', to='profiles.technology'),
        ),
    ]
