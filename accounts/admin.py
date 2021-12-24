from django.contrib import admin
from .models import Account, User, Permission, Role, UserPermission, UserRole, RolePermissions

# Register your models here.

admin.site.register(Account)
admin.site.register(User)
admin.site.register(UserRole)
admin.site.register(UserPermission)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(RolePermissions)
