# Generated by Django 3.1.3 on 2021-09-06 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210906_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='created_at',
            field=models.DateField(default=1630919465.1728468),
        ),
    ]
