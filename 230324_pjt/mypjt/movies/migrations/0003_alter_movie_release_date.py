# Generated by Django 3.2.18 on 2023-03-24 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_rename_article_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(auto_now=True),
        ),
    ]
