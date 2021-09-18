from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns=[


    path('log/',views.Loginview,name='login'),
    path('logo/',views.logoutview,name='logout'),
    path('register/',views.userregister,name='register'),
    path('home/',views.homeview,name='home'),
    
    path('change/',views.changepasswordview,name='cpass'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
