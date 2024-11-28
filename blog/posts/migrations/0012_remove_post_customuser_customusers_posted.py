# Generated by Django 4.1.7 on 2023-10-26 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_post_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='customuser',
        ),
        migrations.AddField(
            model_name='customusers',
            name='posted',
            field=models.ManyToManyField(to='posts.post'),
        ),
    ]