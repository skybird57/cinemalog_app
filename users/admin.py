from django.contrib import admin
from django.contrib.auth.models import Group,User  #unregister
from users.models import CustomUser,CustomUserToken
from django_jalali.admin import jDateTimeField,JDateFieldListFilter
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('phone','score',)
    list_filter=(('created_at',JDateFieldListFilter),)
    search_fields=('phone',)
class UserTokenAdmin(admin.ModelAdmin):
    list_display=('token','user',)
 

#register
admin.site.register(CustomUser,UserAdmin)
admin.site.register(CustomUserToken,UserTokenAdmin)
#unregister
admin.site.unregister(Group)
