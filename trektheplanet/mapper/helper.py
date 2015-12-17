
from django.shortcuts import render
from django.http import HttpResponse 
from django.core import serializers
from .models import Destination
import json

def collect_coordinates():
	s = serializers.serialize("json", Destination.objects.filter(approved=True))
	dests = json.loads(s)
	#coordinates = []
	return dests
	#return coordinates

def compute_international():
#computes the best way to connect the strongly connected components that make up each country
#connecting country to country
#returns the path of the countries connections
	s = serializers.serialize("json", Destination.objects.filter(base=True))
	path = json.loads(s) 
	print(json.dumps(path)) 
#the default of this is just selecting the coordinates that are marked as a base in each country
	return path



	
	
	
def collect_travel_data(coor): 
	pass
	
def compute_cost_path(coor): 
	pass

	
def compute_distance_path(coor):
	pass
	

