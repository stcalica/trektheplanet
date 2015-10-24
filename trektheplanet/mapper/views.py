from django.shortcuts import render
from django.http import HttpResponse 
from django.core import serializers
from .models import Destination

import json

def index(request):
		
	s = serializers.serialize("json", Destination.objects.all())
	dests = json.loads(s)
	coordinates = []
	i = 0 
	for d in dests: 
		coor = "{\"lat\":"+ str(dests[i]["fields"]["latitude"])+",\"lng\":"+ str(dests[i]["fields"]["longitude"])+ "}"
		i = i + 1
		print(i) 
		print(coor) 
		coordinates.append(coor)

	return render(request, "index.html", {'coordinates' : coordinates })
