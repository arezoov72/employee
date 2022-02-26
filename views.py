from django.shortcuts import render,HttpResponse,Http404,redirect
import pymongo
from .models import employee
import os
from django.db.models import Q
from django.contrib.auth.models import User


# Create your views here.

def index(request):
 
    cooprators=employee.objects.all()
    if 'term' in request.GET:
        qs=employee.objects.filter(
            Q(firstname__istartswith=request.GET.get('term'))|
            Q(lastname__istartswith=request.GET.get('term'))|
            Q(post__icontains=request.GET.get('term'))|
            Q(tell__istartswith=request.GET.get('term'))|
            Q(EmploymentDate__istartswith=request.GET.get('term'))
            
            )

        titles=list()
        for Employee in qs:
            titles.append(Employee.firstname)
            titles.append(Employee.lastname)
            
        return JsonResponse(titles, safe=False)
    # ip of clients
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip)
    return render(request,'cooprator.html',{'ip':ip})



from django.http import JsonResponse
def cooprators(request):
    cooprators=employee.objects.all()
    
    if 'term' in request.GET:
        qs=employee.objects.filter(
            Q(firstname__istartswith=request.GET.get('term'))|
            Q(lastname__istartswith=request.GET.get('term'))|
            Q(post__icontains=request.GET.get('term'))|
            Q(tell__istartswith=request.GET.get('term'))|
            Q(EmploymentDate__istartswith=request.GET.get('term'))
            
            )

        titles=list()
        for Employee in qs:
            titles.append(Employee.firstname)
            titles.append(Employee.lastname)
            
        return JsonResponse(titles, safe=False)
        

     

    return render(request,'coorperators1.html',{'cooprators':cooprators})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip)
    return HttpResponse(ip)


def search(request):

    allstaff=employee.objects.all()
    query=request.GET.get("Employee")
    if query:
        
        allstaff=employee.objects.filter(
            Q(lastname__icontains=query) |
            Q(firstname__icontains=query) |
            Q(post__icontains=query) |
            Q(tell__icontains=query) |
            Q(EmploymentDate__icontains=query) |
            
            Q(Email__icontains=query) 
            
        ).distinct()
     

    return render(request,'search.html',{'allstaff':allstaff})


from django.http import HttpResponse 
  
def index_page(request):
   

 

    html = (
        "<html><body><h1>Imagine there's a list of blog posts here!</h1></body></html>"
    )
    return redirect('/index')




import json
def autocomplete(request):
    allstaff=employee.objects.all()
    if 'term' in request.GET:
        qs=employee.objects.filter(
            Q(firstname__istartswith=request.GET.get('term'))|
            Q(lastname__istartswith=request.GET.get('term'))|
            Q(post__icontains=request.GET.get('term'))|
            Q(tell__istartswith=request.GET.get('term'))|
            Q(EmploymentDate__istartswith=request.GET.get('term'))
            
            ).exclude(postid=70)

        titles=list()
        for Employee in qs:
            titles.append(Employee.firstname)
            titles.append(Employee.lastname)
            
        return JsonResponse(titles, safe=False)



    return render(request,'search.html',{'allstaff':allstaff})     
    



def members(request):


    members=employee.objects.all().exclude(postid=70)
    
    if 'term' in request.GET:
        qs=employee.objects.filter(
            Q(firstname__istartswith=request.GET.get('term'))|
            Q(lastname__istartswith=request.GET.get('term'))|
            Q(post__icontains=request.GET.get('term'))|
            Q(tell__istartswith=request.GET.get('term'))|
            Q(EmploymentDate__istartswith=request.GET.get('term'))
            
           ).exclude(postid=70)

        titles=list()
        for Employee in qs:
            titles.append(Employee.firstname)
            titles.append(Employee.lastname)
            
        return JsonResponse(titles, safe=False)
    return render(request,'members.html',{'members':members})





