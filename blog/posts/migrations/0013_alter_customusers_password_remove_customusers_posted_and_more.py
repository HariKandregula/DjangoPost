# Generated by Django 4.1.7 on 2024-02-10 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_remove_post_customuser_customusers_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusers',
            name='password',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.RemoveField(
            model_name='customusers',
            name='posted',
        ),
        migrations.AlterField(
            model_name='customusers',
            name='username',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customusers',
            name='posted',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.post'),
        ),
    ]
