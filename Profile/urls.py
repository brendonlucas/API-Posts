from django.urls import path
from Profile import views
from Profile.views import *

urlpatterns = [
    path('', ApiRoot.as_view(), name=ApiRoot.name),
    path('profile/', ProfileList.as_view(), name=ProfileList.name),
    path('profile/<int:pk>', ProfileDetail.as_view(), name=ProfileDetail.name),

    path('profile-post/', ProfilePostlist.as_view(), name=ProfilePostlist.name),
    path('profile-post/<int:pk>', ProfilePostDetail.as_view(), name=ProfilePostDetail.name),
]