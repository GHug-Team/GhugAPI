# Generated by Django 4.0.4 on 2022-06-23 23:27

from django.db import migrations, models
import news.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(blank=True, max_length=255, upload_to=news.models.upload_to),
        ),
    ]