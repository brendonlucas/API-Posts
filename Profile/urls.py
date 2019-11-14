from django.urls import path, include
from Profile import views
from Profile.views import *

urlpatterns = [
    path('', ApiRoot.as_view(), name=ApiRoot.name),
    path('profile/', ProfileList.as_view(), name=ProfileList.name),
    path('profile/<int:pk>', ProfileDetail.as_view(), name=ProfileDetail.name),

    path('profile-post/', ProfilePostlist.as_view(), name=ProfilePostlist.name),
    path('profile-post/<int:pk>', ProfilePostDetail.as_view(), name=ProfilePostDetail.name),

    path('info/', views.info, name='info'),
    path('import-dados/', views.import_dados, name='import-dados'),

    path('users/', views.UserList.as_view(), name=views.UserList.name),

    path('users/<int:pk>/', views.UserDetail.as_view(), name=views.UserDetail.name),
    path('api-auth/', include('rest_framework.urls'))
]
