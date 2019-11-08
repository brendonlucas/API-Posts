from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Profile.urls')),
    path('', include('Posts.urls'))
]
