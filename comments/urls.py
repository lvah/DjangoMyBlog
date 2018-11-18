from django.conf.urls import url, include
from django.contrib import admin
from comments import views


app_name="comments"
urlpatterns = [
    url(r'^comment/blog/(?P<pk>\d+)/$', views.post_comment, name='post_comment'),


]



# {% load static %}
# {% for %}
