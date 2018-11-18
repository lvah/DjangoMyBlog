from django.conf.urls import url, include
from django.contrib import admin
from blog import views

app_name='blog'
urlpatterns = [
    url(r'^$', views.index,name="index"),
    url(r'^(?P<id>[0-9]+)/$',views.detail,name="detail" ), #name是给视图函数起个别名
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/$', views.archive,
        name='archive'),
    url(r"^category/(?P<id>\d+)/$", views.category, name="category"),
    url(r"^tag/(?P<id>\d+)/$", views.tag, name="tag"),
    url(r"^search/$", views.search, name="search")

]