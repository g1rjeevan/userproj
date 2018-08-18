from django.conf.urls import url

from category import views
from category.views import get_search

urlpatterns = [
    url(r'^categories/$', views.CategoryList.as_view(), name='category-list'),
    url(r'^categories-sorted/$', views.CategoryFilterList.as_view(), name='category-filter-list'),
    url(r'^categories/(?P<pk>[\w\-]+)/$', views.CategoryDetail.as_view(), name='category-detail'),
    url(r'^(?P<param>[-\w]+)/$', get_search, name='Get Results'),
]
