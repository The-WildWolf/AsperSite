# Generated by Django 3.2.13 on 2022-06-03 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='featured_image/%Y/%m/%d/'),
        ),
    ]
