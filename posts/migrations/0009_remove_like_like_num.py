# Generated by Django 4.2.4 on 2023-08-06 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_remove_post_like_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='like_num',
        ),
    ]
