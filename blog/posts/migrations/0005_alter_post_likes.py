# Generated by Django 4.1.7 on 2023-06-19 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
