from django.db import models
from django_jalali.db import models as jmodel
from django.utils.translation import ugettext as _

# Create your models here

class User(models.Model):
    username=models.CharField(_('username'),max_length=30,blank=True, null=True)
    phone=models.CharField(_('phone'),max_length=11)
    image=models.FileField(_('image'),blank=True, null=True)
    address=models.TextField(_('address'),max_length=300,blank=True, null=True)
    notification_status=models.BooleanField(_('notification_status'),default=False)
    created_at=jmodel.jDateTimeField(_('create_at'),blank=True, null=True)
    updated_at=jmodel.jDateTimeField(_('updated_at'),blank=True, null=True)


    def __str__(self):
        return self.phone
    class Meta:
        verbose_name=_('User')
        verbose_name_plural=_('Users')

class UserToken(models.Model):
    token=models.TextField(_('token'),max_length=500)
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name=_('user_id'))

    def __str__(self):
        return self.token
    class Meta:
        verbose_name=_('UserToken')
        verbose_name_plural=_('UserTokens')