from django.db import models

# Create your models here.


class Destination(models.Model):
	location = models.CharField(max_length=18)
	country = models.CharField(max_length=18)
	latitude = models.FloatField()
	longitude = models.FloatField()



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