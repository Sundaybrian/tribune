# Generated by Django 2.2.4 on 2019-08-22 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_editor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='', upload_to='articles'),
        ),
    ]
