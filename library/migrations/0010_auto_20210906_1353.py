# Generated by Django 3.1.3 on 2021-09-06 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_auto_20210906_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumtrack',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_track', to='library.album'),
        ),
        migrations.AlterField(
            model_name='list',
            name='create_at',
            field=models.DateField(default=1630925601.545444),
        ),
    ]
