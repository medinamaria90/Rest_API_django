# Generated by Django 5.0.4 on 2024-04-25 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GithubUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('github_url', models.URLField(max_length=255, unique=True)),
                ('avatar_url', models.URLField(default='', max_length=255, unique=True)),
                ('public_repos', models.IntegerField(default=0)),
            ],
        ),
    ]