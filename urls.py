from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import auth
from django.contrib.auth import login,views as auth_views



urlpatterns = [
    path('',views.index,name='index'),
    path('index2/',views.cooprators,name='cooprators'),
    path('search/',views.search,name='search'),
    path('members/',views.members,name='members'),
    path('members2/',views.members2,name='members'),
    path('members3/',views.members3,name='members'),
    path('members4/',views.members4,name='members'),
    path('members6/',views.members6,name='members'),
    path('members7/',views.members7,name='members'),
    path('members8/',views.members8,name='members'),
    path('members9/',views.members9,name='members'),
    path('members10/',views.members10,name='members'),
    path('members11/',views.members11,name='members'),
    path('members12/',views.members12,name='members'),
    path('members13/',views.members13,name='members'),
    path('members14/',views.members14,name='members'),
    path('members15/',views.members15,name='members'),
    path('members16/',views.members16,name='members'),
    path('ip/',views.get_client_ip,name='get_client_ip'),
    path('autocomplete/',views.autocomplete,name='autocomplete'),
    path('repo/',views.index_page,name='index_page'),
    
    

   

    #authentication,login,pass and reser pass
    path('', include('django.contrib.auth.urls')),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html')),        
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'), 
   
    
   
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


