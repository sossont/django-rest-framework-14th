# Generated by Django 3.0.8 on 2021-10-31 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211101_0154'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Likes',
            new_name='Like',
        ),
        migrations.RenameModel(
            old_name='Videos',
            new_name='Video',
        ),
    ]
