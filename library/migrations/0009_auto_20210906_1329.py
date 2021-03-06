# Generated by Django 3.1.3 on 2021-09-06 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20210906_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='create_at',
            field=models.DateField(default=1630924148.0838473),
        ),
        migrations.AlterField(
            model_name='track',
            name='artists',
            field=models.ManyToManyField(related_name='artist_tracks', through='library.TrackArtist', to='library.Artist'),
        ),
    ]
