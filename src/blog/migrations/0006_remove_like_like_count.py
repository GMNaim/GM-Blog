# Generated by Django 3.0.4 on 2020-03-06 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_delete_postview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='like_count',
        ),
    ]
