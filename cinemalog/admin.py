from django.contrib import admin
from .models import Video,Competition,Question,Gift,SendPush,SendAdv,ApplicationVersion,News
from django_jalali.admin import JDateFieldListFilter # user persian calendar in search admin
from rangefilter.filter import DateRangeFilter  #range for date,pip install django-admin-rangefilter
from django import forms #use in modelform
from django.forms import TextInput,Textarea,ModelForm # use in widgets modelform
from datetime import datetime #update published
from django.urls import reverse # use in comptition
from django.utils.html import format_html #use in competition
# Register your models here.

class VideoForm(ModelForm):
    class Meta:
        model=Video
        fields='__all__'
        
       #labels={
        #    'film_name':'',
         #   'desc':'',
          #  'create_at':''
        #}
        widgets={
            'film_name':TextInput(attrs={'placeholder':"نام فیلم را وارد کنید"}),
            'desc':Textarea(attrs={'placeholder':" یک دیالوگ از فیلم(ترجیحا 160 کاراکتر)...",'rows':4, 'cols':85}),
            #'create_at':jadmin.widgets.AdminjDateWidget.(attrs={'placeholder':"تاریخ آپلود فیلم"})
        }
class VideoAdmin(admin.ModelAdmin):
    form=VideoForm
    #tarz namayesh dar we admin
    list_display=('film_name','published','published_at','adminCoverVideo','create_at')
    #namayesh tarikh jalali
    list_filter=(('create_at',JDateFieldListFilter),'published')
    search_fields=('film_name',)
    #sakht action balaye safhe
    actions=['make_published']
    # be sorat id nmayesh bede
    #raw_id_fields=('user',)
    #fied user_id ro neshon nade
    exclude=('user','published','published_at','create_at')
    #exclude=(,)

    def make_published(modeladmin,request,queryset):
        if 'cinemalog.publish_video' in request.user.get_all_permissions():
            queryset.update(published=True,published_at=datetime.date.today())
            
    make_published.short_description='mark selected video as  pblished'
    make_published.allow_tags=True

    def get_actions(self,request):       
        actions = super(VideoAdmin, self).get_actions(request)
        if 'cinemalog.publish_video' not in request.user.get_all_permissions():
             del actions['make_published']
        return actions

    def adminCoverVideo(self,obj):
        from django.utils.safestring import mark_safe
        from Cinemalogs.settings import MEDIA_URL
        #use when save by save_mode
        #return mark_safe('<img src="{}" width=100px height=100px/>'.format(MEDIA_URL+
         #               '/'+obj.film_name+'/'+str(obj.cover_video)))
        # this return is for upload_to im model.py
        return mark_safe('<img src="{}" width=100px height=100px/>'.format(MEDIA_URL+str(obj.cover_video)))
    adminCoverVideo.allow_tag=True
    # methos save mibashad, yani ghabl az save user_id=currentuser kon bad save kon
    def save_model(self, request, obj, form, change):
        obj.user=request.user
        if 'cinemalog.publish_video'  not in request.user.get_all_permissions():
            obj.published=False
        #save file to media dir+save name file to field
        '''from django .conf import settings
        from django.core.files.storage import FileSystemStorage
        fs=FileSystemStorage(location=settings.MEDIA_ROOT+'/'+obj.film_name)
        videofile=request.FILES['file_name']
        obj.file_name=fs.save(videofile.name,videofile)
        coverfile=request.FILES['cover_video']    
        obj.cover_video=fs.save(coverfile.name,coverfile)
        '''
        return super().save_model(request, obj, form, change)
    #delete files and folder
    def delete_model(self, request, obj):
        from Cinemalogs.settings import MEDIA_ROOT
        import shutil
        try:
            path=MEDIA_ROOT+'\\MEDIA_ROOT\\'+obj.film_name               
            shutil.rmtree(path)
        except OSError as e:
            return e
        return super().delete_model(request, obj)

class CompetitionAdmin(admin.ModelAdmin):
    #tarz namayesh dar we admin
    list_display=('title','create_at','list_questions')
    #namayesh tarikh jalali
    list_filter=(('create_at',JDateFieldListFilter),)

    def list_questions(self,obj):
        link=reverse("admin:cinemalog_question_changelist")
        return format_html('<a href="{0}?q={1}">لیست سوالات {2} </a>'.format(link, obj.title,obj.title   ))
    list_questions.allow_tags=True   
    #list_questions=_('list_ques')  

class QuestionAdmin(admin.ModelAdmin):
    #tarz namayesh dar we admin
    list_display=('question','correct_answer','link_competition')
    #tabdile key khareji jadvale question be title dar jadvale competition
    def link_competition(self,obj):
        link= reverse("admin:cinemalog_competition_change", args=[obj.Competition.id]) #model name has to be lowercase
        #return u'%s' % (obj.Competition.title)
        return format_html('<a href="{}"> {}</a>', link, obj.Competition.title)
    link_competition.allow_tags=True

    Ordering=('competition_id',)
    list_filter=('Competition__title',)
    search_fields=('Competition__title','question','correct_answer')

class GiftAdmin(admin.ModelAdmin):
    list_display=('title','desc','deliverDate')
    list_filter=(('deliverDate',DateRangeFilter),'deliverDate',)
    search_fields=('title',)
    

class SendPushAdmin(admin.ModelAdmin):
    list_display=('title','content','platform_android','platform_ios')
    list_filter=('platform_android','platform_ios')
    search_fields=('title','content')
    prepopulated_fields={'content':('title',)}
    exclude=('user',)

    def save_model(self, request, obj, form, change):
        obj.user=request.user
        if obj.platform_android and obj.platform_ios:
            obj.content+="   this push is sendin to all devices"
        elif obj.platform_ios:
            obj.content+="   this push is sending for IOS devices"
        elif obj.platform_android:
            obj.content+="   this push is sending for Android devices"   


        return super().save_model(request, obj, form, change)

class SendAdvAdmin(admin.ModelAdmin):
    list_display=('title','content','adv_type','platform_android','platform_ios')
    list_filter=('platform_android','platform_ios','adv_type')
    search_fields=('title','content')
    prepopulated_fields={'content':('title',)}

class ApplicationVersionAdmin(admin.ModelAdmin):
    list_display=('platform','require_version','last_version','generated_at')
    list_filter=(('generated_at',JDateFieldListFilter),'platform')
    search_fields=('require_version','last_version')
    exclude=('user',)
    def save_model(self, request, obj, form, change):
        obj.user=request.user
        return super().save_model(request, obj, form, change)


class NewsAdmin(admin.ModelAdmin):
    #fields=('title','admin_image',)
    list_display=('title','desc','admin_image','published_at')
    readonly_fields=('admin_image',)
    search_fields=('title','desc',)
    list_filter=('published_at',)
    def admin_image(self,obj):
        from django.utils.safestring import mark_safe
        return mark_safe('<img src="{}" width=144px/>'.format(obj.image))
    #admin_image.short_description="Image"    
    admin_image.allow_tag=True 

   
admin.site.register(Video,VideoAdmin)
admin.site.register(Competition,CompetitionAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Gift,GiftAdmin)
admin.site.register(SendPush,SendPushAdmin) 
admin.site.register(SendAdv,SendAdvAdmin)
admin.site.register(ApplicationVersion,ApplicationVersionAdmin)
admin.site.register(News,NewsAdmin)