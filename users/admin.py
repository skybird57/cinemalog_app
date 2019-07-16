from django.contrib import admin
from django.contrib.auth.models import Group,User  #unregister

# Register your models here.


admin.site.unregister(Group)
