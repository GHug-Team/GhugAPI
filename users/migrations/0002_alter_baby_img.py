# Generated by Django 4.0.4 on 2022-05-29 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baby',
            name='img',
            field=models.ImageField(blank=True, max_length=255, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
