from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django_jalali.db import models as jmodels


# Create your models here.



class post(models.Model):
    postid=models.IntegerField(default=1)
    posttitle=models.CharField(max_length=255)





class employee(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    firstname=models.CharField(max_length=255,db_column='firstname')
    lastname=models.CharField(max_length=255,db_column='lastname')
    post=models.CharField(max_length=255,db_column='post')
    tell=models.IntegerField(null=False,blank=True,db_column='tell')
    image=models.ImageField(upload_to='pictures/',blank=True,null=True,db_column='image')
    postid=models.IntegerField(default=1,db_column='postid')
    Email=models.CharField(null=True,max_length=255,db_column='Email')
    managerid=models.IntegerField(null=True,db_column='managerid')
    username=models.ForeignKey(User,on_delete=models.CASCADE,max_length=30,null=True,to_field='username',db_column='username')
    mobile=PhoneField(blank=True,default=0)
    birthdate=jmodels.jDateField(null=True)
    EmploymentDate=jmodels.jDateField(null=True)

    def __str__(self):
        return "%s, %s" % (self.lastname, self.birthdate)

    class Meta:
        permissions = [('is_manager', 'Can see employee'),('is_employee', 'Can see self')]

        db_table = 'employee'
    
    


    #def __str__(self):
       # return self.postid

        #postid=models.ForeignKey(post,on_delete=models.CASCADE)

        

      







