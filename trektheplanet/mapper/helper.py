
from django.shortcuts import render
from django.http import HttpResponse 
from django.core import serializers
from .models import Destination
import json

def collect_coordinates():

		
	s = serializers.serialize("json", Destination.objects.all())
	dests = json.loads(s)
	#coordinates = []
	"""
	i = 0 
	for d in dests: 
	coor = "{\"lat\":"+ str(dests[i]["fields"]["latitude"])+",\"lng\":"+ str(dests[i]["fields"]["longitude"])+",\"location\":\" " +str(dests[i]["fields"]["location"])+"\"}"
	i = i + 1
	"""
	#coordinates.append(dests)
	return dests
	#return coordinates

def collect_travel_data(): 
	pass
	
def compute_cost_path(): 
	pass

	
def compute_distance_path():
	pass
	
