from django.db import models
from django_countries.fields import CountryField
# Create your models here.


class Destination(models.Model):
	location = models.CharField(max_length=50)
	country = CountryField()
	latitude = models.FloatField()
	longitude = models.FloatField()
	visited   = models.BooleanField()
	approved = models.BooleanField(default='false') 
	base = models.BooleanField(default='false')
	def __unicode__(self):
		return self.location 


class Blog(models.Model): 
	title = models.CharField(max_length=50)
	article = models.TextField() #if video then store file_path
	country = CountryField()
	date = models.DateField() 
	vlog = models.BooleanField(default='True') #if vlog then yes  
	def __unicode__(self):
		return self.title 
		
		
		
class Contact(models.Model):
	name = models.CharField(max_length=50) 
	home = models.CharField(max_length=50) 
	email = models.CharField(max_length=50) 
	country = CountryField()
	phone = models.IntegerField() 
	location = models.ForeignKey('Destination')

	def __unicode__(self):
		return self.name 	
		
"""
class Vlog(models.Model): 
	title = models.CharField(max_length=50)
	file_path = models.CharField()
	date = models.DateField() 
	country = CountryField()
	def __unicode__(self):
		return self.title 
class Contact(models.Model):
	name = models.CharField(25) 
	home = models.CharField(25) 
	latitude = models.FloatField() #latitude and Lng??? 
	longitude = models.FloatField() #latitude and Lng???
	email = models.CharField(25) 
	phonenumber = models.IntegerField() 
"""
