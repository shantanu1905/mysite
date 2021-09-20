"""acer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from home import views
from todo import views as tod # importing views.py  from todo app , we tod to void error as we are importing views from home and todo apps




from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "Acer Admin"
admin.site.site_title = "Acer Admin Portal"
admin.site.index_title = "Welcome to Acer Portal"

urlpatterns = [
    #path('', views.taskList, name='todo'),
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('tasks', tod.taskList, name='tasks'),  #todo list path
    path('passgen', tod.passgen, name='passgen'),  
    path('delete/<int:Taskdata_id>/' , tod.delete, name='delete'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('writes', views.writes, name='writes'),
    

    path('admin/', admin.site.urls)
    
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
