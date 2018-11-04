# Generated by Django 2.0 on 2018-10-27 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0003_documentation_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='documentation',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='commentresponse',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='commentresponse',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='commentresponse',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='documentation',
            name='likes',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='CommentResponse',
        ),
        migrations.DeleteModel(
            name='Documentation',
        ),
    ]
