# Generated by Django 3.0.8 on 2021-10-31 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_num',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='website',
            field=models.URLField(blank=True, max_length=50),
        ),
    ]
