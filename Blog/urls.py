from django.urls import path,re_path
from .import views

urlpatterns = [
    path("",views.PostList,name="post_list"),
    re_path(r'^detail/(?P<pk>[0-9]{1})/$', views.PostDetail,name="post_list"),
    re_path(r'^detail/(?P<pk>[0-9]{2})/$', views.PostDetail,name="post_list"),
    re_path(r'^detail/(?P<pk>[0-9]{3})/$', views.PostDetail,name="post_list"),
    re_path(r'^detail/(?P<pk>[0-9]{4})/$', views.PostDetail,name="post_list"),
    path("<category>/",views.PostCategory,name="post_category"),
    re_path(r'^page/(?P<page>[0-9]{1})/$',views.PageNumber,name="page"),
]