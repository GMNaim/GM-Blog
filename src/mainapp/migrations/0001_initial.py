# Generated by Django 3.0.4 on 2020-03-12 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(default='', max_length=50)),
                ('site_title', models.CharField(default='', max_length=255)),
                ('top_background_img', models.ImageField(upload_to='')),
                ('site_intro_text1', models.TextField(default='')),
                ('middle_background_img', models.ImageField(upload_to='')),
                ('middle_img_title_text', models.TextField(default='')),
                ('newsletter_title', models.CharField(max_length=255)),
                ('newsletter_text', models.TextField(default='')),
                ('facebook_link', models.CharField(default='', max_length=200)),
                ('twitter_link', models.CharField(default='', max_length=200)),
                ('youtube_link', models.CharField(default='', max_length=200)),
                ('instagram_link', models.CharField(default='', max_length=200)),
                ('pinterest_link', models.CharField(default='', max_length=200)),
                ('site_email', models.EmailField(max_length=254)),
                ('site_phone', models.CharField(max_length=20)),
                ('settings_name', models.CharField(default='Settings', max_length=30)),
            ],
        ),
    ]
