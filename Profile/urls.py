from django.urls import path
from Profile import views

urlpatterns = [
    path('profiles/', views.profile_list),
    path('profiles/<int:id>/', views.profile_detail),
    path('profilesPosts/', views.profile_post_list),
    path('profilesPosts/<int:id>/', views.profile_post_detail)
]