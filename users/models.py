from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext as _
# Create your models here

class CustomUser(AbstractBaseUser):
    username=models.CharField(_('username'),max_length=30)
    email=models.CharField(_('email'),max_length=50)
    password=models.CharField(_('password'),max_length=300)
    phone=models.CharField(_('phone'),max_length=11)
    is_active=models.BooleanField(_('is_active'),default=False)

    def __str__(self):
        return username+'  '+email
    class Meta:
        verbose_name=_('USer')
        verbose_name_plural=_('Users')