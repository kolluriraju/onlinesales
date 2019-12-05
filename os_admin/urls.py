"""onlinesales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from os_admin import views

urlpatterns = [
    path('adminhome/',TemplateView.as_view(template_name='os_admin_template/os_admin_home.html')),
    path('mainhome/',TemplateView.as_view(template_name='os_main_template/main_galary.html')),
    path('adminlogincheck/',views.adminlogincheck,name="adminlogincheck"),
    path('adminotpcheck/',views.adminotpcheck),
    path('agentsave/',views.agentsave),
    path('agentregister/',views.agentregister),
    path('agentdelete/',views.agentdelete),
    path('adminlogout/', views.adminlogout),
    path('agentupdate/',views.agentupdate),
    path('deleteagent/',views.deleteview),
    path('deleteclient/',views.deleteclient),
    path('client/',views.viewallClients),
    path('propertyall/',views.propertyAll),

]

