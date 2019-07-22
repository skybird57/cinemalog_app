from django.contrib import admin
from django.contrib.auth.models import Group,User  #unregister
from users.models import User,UserToken
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    display_list=('username','phone')
    pass

class UserTokenAdmin(admin.ModelAdmin):
    display_list=('user','token')
    pass

#register
admin.site.register(User,UserAdmin)
admin.site.register(UserToken,UserTokenAdmin)
#unregister
admin.site.unregister(Group)
