# Generated by Django 4.2.7 on 2023-11-14 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_title', models.CharField(max_length=200)),
                ('artist_name', models.CharField(max_length=200)),
                ('created_at', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
