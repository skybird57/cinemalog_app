from django.db import models
from django_jalali.db import models as jmodel
from django.utils.translation import ugettext as _

# Create your models here

class CustomUser(models.Model):
    username=models.CharField(_('Userusername'),max_length=30,blank=True, null=True)
    phone=models.CharField(_('Userphone'),max_length=11,unique=True)
    image=models.FileField(_('Userimage'),blank=True, null=True)
    address=models.TextField(_('Useraddress'),max_length=300,blank=True, null=True)
    notification_status=models.BooleanField(_('Usernotification_status'),default=False)
    score=models.IntegerField(_('CustomUserscore'),default=0)
    created_at=jmodel.jDateTimeField(_('Usercreate_at'),blank=True, null=True)
    updated_at=jmodel.jDateTimeField(_('Userupdated_at'),blank=True, null=True)


    def __str__(self):
        return self.phone+str(score)
    class Meta:
        verbose_name=_('CustomUser')
        verbose_name_plural=_('CustomUsers')

class CustomUserToken(models.Model):
    token=models.TextField(_('Tokentoken'),max_length=500,unique=True)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,verbose_name=_('Tokenuser_id'))

    def __str__(self):
        return self.token
    class Meta:
        verbose_name=_('UserToken')
        verbose_name_plural=_('UserTokens')