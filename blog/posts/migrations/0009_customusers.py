# Generated by Django 4.1.7 on 2023-10-08 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customusers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
    ]