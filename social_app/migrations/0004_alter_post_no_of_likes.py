# Generated by Django 5.0.1 on 2024-02-02 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0003_likepost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='no_of_likes',
            field=models.IntegerField(default=0),
        ),
    ]
