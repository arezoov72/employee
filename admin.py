from django.contrib import admin
from .models import employee,post

# Register your models here.

#class POSTADMIN(admin.ModelAdmin):
    #list_display('id','postid','managerid')

#class EMPLOYEEADMIN(admin.ModelAdmin):
    #model=employee
    #list_display=['username','firstname']

class POSTADMIN(admin.ModelAdmin):
    list_display=['postid','posttitle']


class MANAGERADMIN(admin.ModelAdmin):
     list_display=['managerfname','managerlname','managerid']
   





#admin.site.register(employee,EMPLOYEEADMIN)
admin.site.register(post,POSTADMIN)



