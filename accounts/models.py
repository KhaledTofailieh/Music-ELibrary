from django.db import models
import time


class Account(models.Model):
    user_name = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=20)
    created_at = models.DateField(default=time.time())
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_name


class Permission(models.Model):
    code = models.CharField(unique=True, max_length=20)
    key = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.code + ", " + self.key


class Role(models.Model):
    code = models.CharField(unique=True, max_length=20)
    key = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.code + ", " + self.key


class RolePermissions(models.Model):
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    added_date = models.DateField(default=time.time())

    class Meta:
        unique_together = ['permission_id', 'role_id']

    def __str__(self):
        return self.role.__str__() + " | " + self.permission.__str__()




class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25, null=True)
    account = models.OneToOneField(Account, on_delete=models.CASCADE, null=True)
    roles = models.ManyToManyField(Role, related_name='user_roles', through='UserRole')
    permissions = models.ManyToManyField(Permission, related_name='user_permissions', through='UserPermission')

    def __str__(self):
        return self.first_name + " " + self.last_name


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    taken_time = models.DateTimeField(null=True)
    expire_time = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True, null=True)

    class Meta:
        unique_together = ['user_id', 'role_id']

    def __str__(self):
        return self.user.__str__() + " | " + self.role.key


class UserPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    taken_time = models.DateField(null=True)
    expire_time = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True, null=True)

    class Meta:
        unique_together = ['user_id', 'permission_id']

    def __str__(self):
        return self.user.__str__() + " | " + self.permission.key
