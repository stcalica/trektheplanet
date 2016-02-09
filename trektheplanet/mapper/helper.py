
from django.shortcuts import render
from django.http import HttpResponse 
from django.core import serializers
from .models import Destination
import json

""" Collect all coordinates and serve it out """

def collect_coordinates():
	s = serializers.serialize("json", Destination.objects.filter(approved=True))
	dests = json.loads(s)
	#coordinates = []
	return dests
	#return coordinates
""" Serve a International Path """

def compute_international():
#computes the best way to connect the strongly connected components that make up each country
#connecting country to country
#returns the path of the countries connections
	s = serializers.serialize("json", Destination.objects.filter(base=True))
	path = json.loads(s)
	nodes = Destination.objects.filter(base=True)
	for node in nodes:	
		print node   
	print(json.dumps(path)) 
#the default of this is just selecting the coordinates that are marked as a base in each country
	return path

""" Suggested Travels  """

def travel_by_price():
	pass

def travel_by_less():
	#travel by less edges
	pass

def travel_by_more():
	#travel by more edges
	pass

	
	
""" Travel API data serve as strings """ 	
def collect_travel_data(coor): 
	pass

""" Compute costs and paths for helper functions  """
	
def compute_cost_path(coor): 
	pass

def compute_distance_path(coor):
	pass
	

