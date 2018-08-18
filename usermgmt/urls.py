from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token

from usermgmt import views
from usermgmt.views import login

urlpatterns = [
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^api-token-auth/', obtain_auth_token),
    url('login/$', login)
]
