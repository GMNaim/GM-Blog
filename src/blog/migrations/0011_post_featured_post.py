# Generated by Django 3.0.4 on 2020-03-13 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200311_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_post',
            field=models.BooleanField(default=False),
        ),
    ]
