from django.urls import path
from Profile import views
from Profile.views import *

urlpatterns = [
    path('', ApiRoot.as_view(), name=ApiRoot.name),
    path('profile/', ProfileList.as_view(), name=ProfileList.name),
    path('profile/<int:id>', ProfileDetail.as_view(), name=ProfileDetail.name),

    path('profile-post/', ProfilePostlist.as_view(), name=ProfilePostlist.name),
    path('profile-post/<int:id>', ProfilePostDetail.as_view(), name=ProfilePostDetail.name),
]



"""
urlpatterns = [
    path('profiles/', views.profile_list),
    path('profiles/<int:id>/', views.profile_detail),
    path('profilesPosts/', views.profile_post_list),
    path('profilesPosts/<int:id>/', views.profile_post_detail)
]

"""