from django.conf.urls import url
from django.contrib import admin
from blog.views import *
urlpatterns = [ 
	url(r'^$',index),
	url(r'^blog/$',get_blogs), 
	url(r'^detail/(\d+)/$',get_details,name='blog_get_detail')
]
