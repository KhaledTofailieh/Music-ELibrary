# Generated by Django 3.1.3 on 2021-09-24 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210924_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='permissions',
            field=models.ManyToManyField(related_name='user_permissions', through='accounts.UserPermission', to='accounts.Permission'),
        ),
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(related_name='user_roles', through='accounts.UserRole', to='accounts.Role'),
        ),
        migrations.AlterField(
            model_name='account',
            name='created_at',
            field=models.DateField(default=1632503912.767102),
        ),
        migrations.AlterField(
            model_name='rolepermissions',
            name='added_date',
            field=models.DateField(default=1632503912.8204758),
        ),
        migrations.AlterField(
            model_name='userpermission',
            name='expire_time',
            field=models.DateTimeField(default=1632503912.8204758, null=True),
        ),
        migrations.AlterField(
            model_name='userpermission',
            name='taken_time',
            field=models.DateField(default=1632503912.8204758),
        ),
        migrations.AlterField(
            model_name='userrole',
            name='expire_time',
            field=models.DateTimeField(default=1632503912.8204758, null=True),
        ),
        migrations.AlterField(
            model_name='userrole',
            name='taken_time',
            field=models.DateField(default=1632503912.8204758),
        ),
    ]
