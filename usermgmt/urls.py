from django.urls import include, path

from usermgmt import views

urlpatterns = [
    path('users/', views.UserListView.as_view()),
]