# Generated by Django 3.0.4 on 2020-03-12 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20200312_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagesettings',
            name='address',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='homepagesettings',
            name='facebook_link',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='homepagesettings',
            name='instagram_link',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='homepagesettings',
            name='middle_background_img',
            field=models.ImageField(upload_to='blog_pics/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='homepagesettings',
            name='pinterest_link',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='homepagesettings',
            name='site_phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='homepagesettings',
            name='top_background_img',
            field=models.ImageField(upload_to='blog_pics/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='homepagesettings',
            name='twitter_link',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='homepagesettings',
            name='youtube_link',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
