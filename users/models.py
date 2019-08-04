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
    created_at=jmodel.jDateField(_('Usercreate_at'),blank=True, null=True)
    updated_at=jmodel.jDateField(_('Userupdated_at'),blank=True, null=True)
    verifyCode=models.IntegerField(_('UserVerifyCode'),default=0)


    def __str__(self):
        return self.phone+'___score_'+str(self.score)
    class Meta:
        verbose_name=_('CustomUser')
        verbose_name_plural=_('CustomUsers')

class CustomUserToken(models.Model):
    DEVICE_TYPE=((0,'Ios'),(1,'Android'))
    token=models.TextField(_('Tokentoken'),max_length=500,unique=True)   
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,verbose_name=_('Tokenuser_id'))
    deviceType=models.IntegerField(_('TokenDeviceType'),choices=DEVICE_TYPE)  # tpe device
    deviceId=models.CharField(_('TokenDeviceId'),max_length=200)  # serial id device
    validToken=models.TextField(_('TokenValidToken'),max_length=500) #comes from google


    def __str__(self):
        return self.token
    class Meta:
        verbose_name=_('UserToken')
        verbose_name_plural=_('UserTokens')