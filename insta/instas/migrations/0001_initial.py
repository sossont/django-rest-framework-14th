# Generated by Django 3.0.8 on 2021-10-07 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=30)),
                ('title', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('comments', models.TextField()),
                ('likes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('user_pw', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='instas.Users')),
                ('user_name', models.CharField(max_length=20)),
                ('website', models.CharField(max_length=40)),
                ('introduction', models.TextField()),
                ('phone_num', models.IntegerField()),
                ('gender', models.CharField(max_length=6)),
                ('followers', models.IntegerField()),
                ('following', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('video_id', models.AutoField(primary_key=True, serialize=False)),
                ('video_url', models.FileField(upload_to='post/Videos')),
                ('date', models.DateTimeField()),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instas.Posts')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instas.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('story_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instas.Users')),
            ],
        ),
        migrations.AddField(
            model_name='posts',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instas.Users'),
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('photo_id', models.AutoField(primary_key=True, serialize=False)),
                ('photo_url', models.ImageField(upload_to='post/Photos')),
                ('date', models.DateTimeField()),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instas.Posts')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instas.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instas.Posts')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instas.Users')),
            ],
        ),
    ]