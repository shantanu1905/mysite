from django.contrib import admin
from django.urls import path , include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('contact', include('contact.urls')),
    path('login', include('login.urls')),
    path('register', include('register.urls')),
    path('logout', include('logout.urls')),
    path('tasks', include('tasks.urls')),
    path('tasklist', include('taskfinal.urls')),
    path('passgen', include('passgen.urls')),
    path('geo', include('geo.urls')),


]