from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


urlpatterns=[
       
        path('show/',views.showfileview,name='show'),
        path('up/',views.model_form_upload,name='up'),
]