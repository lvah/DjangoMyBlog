from django.conf.urls import url, include
from django.contrib import admin
from myForm import views

app_name='myForm'
urlpatterns = [
    url(r'^search_form/$', views.search_form,name="search_form"),
    # url(r'^search1/$', views.search,name="search"),
    url(r'^post/$', views.search_post,name="post"),
    url(r'^login/$', views.login,name="login"),

]