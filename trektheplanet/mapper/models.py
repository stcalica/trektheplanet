from django.db import models
from django_countries.fields import CountryField
# Create your models here.


class Destination(models.Model):
	location = models.CharField(max_length=18)
	country = CountryField()
	latitude = models.FloatField()
	longitude = models.FloatField()
	visited   = models.BooleanField()


#slowly add friends later 
#class Friend(models.Model):
#	name = models.CharField(25) 
#	destination = ForeignKey(Destination) 
"""
class Contact(models.Model):
	name = models.CharField(25) 
	home = models.CharField(25) 
	latitude = models.FloatField() #latitude and Lng??? 
	longitude = models.FloatField() #latitude and Lng???
	email = models.CharField(25) 
	phonenumber = models.IntegerField() 
"""
