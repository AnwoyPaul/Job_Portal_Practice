from django.contrib import admin

from .models import Job,Application

class JobAdmin(admin.ModelAdmin):
  list_display=['title','c_name','location','salary','posted_by','date_posted']

  search_fields=['title','c_name']
  list_filter =['location']

class ApplicationAdmin(admin.ModelAdmin):
  list_display=['applicant','job','date_applied']


admin.site.register(Job,JobAdmin) #this connect the models to admin pannel
admin.site.register(Application,ApplicationAdmin)



