# Generated by Django 2.0 on 2019-01-21 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0008_auto_20190114_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='robot',
            name='humidity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='robot',
            name='temperature',
            field=models.IntegerField(default=0),
        ),
    ]
