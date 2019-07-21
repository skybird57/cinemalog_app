from django.db import models
from django.contrib.auth.models import User #use for 
from django_jalali.db import models as jmodels  #user persian datetime
from django.utils.translation import gettext as _  #use for translation
from Cinemalogs.settings import MEDIA_ROOT

# Create your models here.


#mahale zakhireye file hayei ke ba choose file gerefte mishavad
def file_location(instanc,filename):
    return "MEDIA_ROOT/%s/%s"%(instanc.film_name,filename)

class Video(models.Model):
    #"Fields"
    film_name=models.CharField(_('videoname'),max_length=50)
    #part of dialog
    desc=models.TextField(_('videodesc'),max_length=200)
    create_at=jmodels.jDateField(_('videocreatedate'),auto_now_add=True)
    published=models.BooleanField(_('videopublished'),default=False)
    published_at=jmodels.jDateField(_('videopublishdate'),blank=True,null=True) 
    #use upload_to
    file_name=models.FileField(_('videofilename'),upload_to=file_location,max_length=50)
    cover_video=models.FileField(_('videocver'),upload_to=file_location,blank=True,null=True,max_length=50)
    #save by admin.py method save
    #file_name=models.FileField(_('videofilename'),max_length=50)
    #cover_video=models.FileField(_('videocver'),blank=True,null=True,max_length=50)
     
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name=_('user_id'))
    #or
    #from django.conf import settings
    #user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name=_('user_id'))

    def __str__(self):
        return self.film_name+'-'+self.desc

    class Meta:
        permissions=(('publish_video','Can publish video'),
        )
        verbose_name=_("Video")
        verbose_name_plural=_("Videos")

class Competition(models.Model):
    title=models.CharField(_('competitiontitle'),max_length=50)
    #estefade az tarikh jalali
    create_at=jmodels.jDateField(_('competitioncreatedate'))
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name=_("Competition")
        verbose_name_plural=_("Competitions")    

class Question(models.Model):
    SCORE_CORRECT_ANSWER=((1,1),(2,2),(3,3),(4,4),(5,5))
    SCORE_WRONG_ANSWER=((-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5))
    Competition=models.ForeignKey(Competition,on_delete=models.CASCADE)
    question=models.TextField(_('questionuestion'),max_length=100)
    answer1=models.CharField(_('questionanswer1'),max_length=30)
    answer2=models.CharField(_('questionanswer2'),max_length=30)
    answer3=models.CharField(_('questionanswer3'),max_length=30)
    answer4=models.CharField(_('questionanswer4'),max_length=30)
    correct_answer=models.CharField(_('questioncorrect'),max_length=30)
    score_ca=models.IntegerField(_('questionscore_ca'),null=True,choices=SCORE_CORRECT_ANSWER)
    score_wa=models.IntegerField(_('questionscore_wa'),null=True,choices=SCORE_WRONG_ANSWER)
    
    def __str__(self):
        return self.question
    class Meta:
        verbose_name=_("Question")
        verbose_name_plural=_("Questions")    

class Gift(models.Model):
    title=models.CharField(_('gifttitle'),max_length=30)
    desc=models.TextField(_('giftdesc'),max_length=200)
    pic= models.FileField(_('giftpic'),null=True)
    deliverDate=jmodels.jDateField(_('giftdeliverdate'))

class SendPush(models.Model):
    title=models.CharField(_('sendpushtitle'),max_length=30)
    content=models.TextField(_('sendpushcontent'),max_length=200)
    platform_android=models.BooleanField(_('sendpushandroid'),default=False)
    platform_ios=models.BooleanField(_('sendpushios'),default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name=_('user_id'))

    def __str__(self):
        return self.title
    class Meta:
        verbose_name=_('SendPush')
        verbose_name_plural=_('SendPushs')    

class SendAdv(models.Model):
    ADV_TYPE=(
        ('introduce app','معرفی اپلیکیشن'),
        ('introduce game','معرفی بازی')
    )
    title=models.CharField(_('sendadvtitle'),max_length=30)
    content=models.TextField(_('sendadvcontent'),max_length=200)
    adv_type=models.CharField(_('sendadvtype'),choices=ADV_TYPE,max_length=30)
    link=models.URLField(_('sendadvlink'))
    pic=models.FileField(_('sendadvpic'),max_length=30)
    platform_android=models.BooleanField(_('sendadvandroid'),default=False)
    platform_ios=models.BooleanField(_('sendadvios'),default=False)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name=_('SendAdv')
        verbose_name_plural=_('SendAdv')            

class ApplicationVersion(models.Model):
    PLATFORM=((1,'Android'),(2,'IOS'))
    platform=models.IntegerField(_('applicationplatform'),choices=PLATFORM)
    required_version=models.FloatField(_('applicationrequire'),max_length=5)        
    last_version=models.FloatField(_('applicationlast'),max_length=5)
    generated_at=jmodels.jDateField(_('applicationgeneratedate'))
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name=_('user_id'))

    def __str__(self):
        return str(self.platform)+'_____'+str(self.last_version)
    class Meta:
        verbose_name=_('ApplicationVersion')
        verbose_name_plural=_('ApplicationVersions')
        
class News(models.Model):
    title=models.CharField(_('newstitle'),max_length=200)
    desc=models.TextField(_('newsdesc'),max_length=500)
    image=models.URLField(_('newsimage'),null=True)
    source=models.URLField(_('newssource'),null=True)
    published_at=models.CharField(_('newspublished'),max_length=100,null=True,blank=True)

    def __str__(self):
        return self.title+'    '+self.published_at

    class Meta:
        verbose_name=_('News')
        verbose_name_plural=_('News')                       