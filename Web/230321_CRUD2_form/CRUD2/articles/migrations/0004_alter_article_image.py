# Generated by Django 3.2.18 on 2023-03-21 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='articles/%Y%m%d'),
        ),
    ]
