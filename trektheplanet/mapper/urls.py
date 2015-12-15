from django.conf.urls import include, url 
from django.contrib import admin 

from . import views


urlpatterns = [

	url(r'^$', views.index, name='index'),
	url(r'^experience', views.addexp, name='experience'),
	url(r'^about', views.about, name='about'),
	url(r'^vlogs', views.vlogs, name='vlogs'),
	url(r'^pictures', views.pics, name='pictures'),	
	url(r'^donate', views.donate, name='donate'),
	url(r'^contact', views.contact, name='contact'),


]
