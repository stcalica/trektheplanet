from django.shortcuts import render
from django.http import HttpResponse 
from django.core import serializers
from .models import Destination
from .forms import ExpForm 


import urllib2
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


def addexp(request):
	
	if (request.method == "POST"):
		form = ExpForm(request.POST) # need to add the additions and etc like in torrentwidow
		if(form.is_valid()):
			coords = Destination.objects.all()
			num = len(coords) + 1 
			data = form.cleaned_data
			grequest = "https://maps.googleapis.com/maps/api/geocode/json?address=%s" % data["address"]
			print(grequest) 
			response = urllib2.urlopen(grequest)
			geocode = response.read() #convert into json object extract lat and lng then save them to server with Destination object
			print(geocode) 
			#return a thank you alert and then send them to index to see the location added to the map!
			#need to also verify with captchas 
	else:
		form = ExpForm() 
		return render(request, "experience.html", {'form': form}) #form may be wrong but render info and then form underneath


def donate(request):
	# render all donations front for organizations/NGOs/Nonprofits
	# have top parts for us and specific donations request(specifically goes to us and then we do what they ask) 
	# have urls to donate directly 
	return render(request, "donate.html") #may have to do forms to do donations or set up gofund me or something

def about(request):
	#simple about with introduction video 
	return render(request, "about.html"); 


def contactus(request):
	#sends us email
	return render(request, "contactus.html", {'form': form})
