from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('contact', include('contact.urls')),
    path('signup', include('signup.urls')),
    path('login', include('login.urls')),
    path('logout', include('logout.urls')),
    path('dashboard', include('dashboard.urls')),
    path('writes', include('writes.urls')),
 
 
    

]