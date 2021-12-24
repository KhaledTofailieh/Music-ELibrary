# Generated by Django 3.1.3 on 2021-09-24 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20210924_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='created_at',
            field=models.DateField(default=1632506687.3746831),
        ),
        migrations.AlterField(
            model_name='permission',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='permission',
            name='key',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='role',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='role',
            name='key',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='rolepermissions',
            name='added_date',
            field=models.DateField(default=1632506687.4145055),
        ),
        migrations.AlterField(
            model_name='userpermission',
            name='expire_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='userpermission',
            name='taken_time',
            field=models.DateField(null=True),
        ),
    ]
