# Generated by Django 2.0 on 2018-09-19 14:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thing', '0002_comment_commentresponse'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentation',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='documentation_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
