# Generated by Django 3.2.18 on 2023-03-24 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='Movie',
        ),
    ]
