from django.contrib import admin
from django.contrib.auth.models import Group,User  #unregister
from users.models import CustomUser,CustomUserToken
from django_jalali.admin import jDateTimeField,JDateFieldListFilter
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('phone','score','verifyCode','loadUserPic')
    list_filter=(('created_at',JDateFieldListFilter),)
    search_fields=('phone',)
    def loadUserPic(self,obj):
        from django.utils.safestring import mark_safe
        from Cinemalogs.settings import MEDIA_URL
        location=MEDIA_URL+'/avatar/'+str(obj.image)
        print(location)
        return mark_safe('<img src="{}" width=60px height=60px/>'.format(location))
    loadUserPic.allow_tag=True
class UserTokenAdmin(admin.ModelAdmin):
    list_display=('token','user','deviceId','validToken')
 

#register
admin.site.register(CustomUser,UserAdmin)
admin.site.register(CustomUserToken,UserTokenAdmin)
#unregister
admin.site.unregister(Group)
