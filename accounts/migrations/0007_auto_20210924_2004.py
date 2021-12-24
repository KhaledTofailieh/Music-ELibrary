# Generated by Django 3.1.3 on 2021-09-24 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210906_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('key', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('key', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='created_at',
            field=models.DateField(default=1632503068.1494272),
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taken_time', models.DateField(default=1632503068.5197117)),
                ('expire_time', models.DateTimeField(default=1632503068.5197117, null=True)),
                ('is_active', models.BooleanField(default=True, null=True)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
            options={
                'unique_together': {('user_id', 'role_id')},
            },
        ),
        migrations.CreateModel(
            name='UserPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taken_time', models.DateField(default=1632503068.5349147)),
                ('expire_time', models.DateTimeField(default=1632503068.5349147, null=True)),
                ('is_active', models.BooleanField(default=True, null=True)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.permission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
            options={
                'unique_together': {('user_id', 'permission_id')},
            },
        ),
        migrations.CreateModel(
            name='RolePermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateField(default=1632503068.5197117)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.permission')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.role')),
            ],
            options={
                'unique_together': {('permission_id', 'role_id')},
            },
        ),
    ]
