# Generated by Django 3.1.3 on 2021-09-24 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20210924_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrole',
            name='expire_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='userrole',
            name='is_active',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='userrole',
            name='taken_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='created_at',
            field=models.DateField(default=1632505991.094013),
        ),
        migrations.AlterField(
            model_name='rolepermissions',
            name='added_date',
            field=models.DateField(default=1632505991.1474597),
        ),
        migrations.AlterField(
            model_name='userpermission',
            name='expire_time',
            field=models.DateTimeField(default=1632505991.1474597, null=True),
        ),
        migrations.AlterField(
            model_name='userpermission',
            name='taken_time',
            field=models.DateField(default=1632505991.1474597, null=True),
        ),
    ]