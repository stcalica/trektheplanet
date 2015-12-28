from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from .models import Destination, Blog, Contact
from .forms import ExpForm 
from helper import collect_coordinates,  compute_international
from django.contrib import messages
from django_countries import countries


import urllib
import urllib2
import json

def  index(request):
		
	coordinates = []
	coordinates = collect_coordinates()
	#cost_path = collect_cost_path()
	#distance = collect_distance_path() 
	c = compute_international()
	return render(request, "index.html", {'coordinates' : json.dumps(coordinates), 'int_path' : json.dumps(c), 'codes' : json.dumps(dict(countries))  })

def addexp(request):
	form = ExpForm()
	if (request.method == "POST"):
		form = ExpForm(request.POST) 
		print("Checking if form is valid..") 
		if(form.is_valid()):
			print("form is valid")
			coords = Destination.objects.all()
			num = len(coords) + 1 
			contacts = Contact.objects.all()
			new = len(contacts) + 1 
			data = form.cleaned_data
			#add address and country together then put in request 
			grequest = "https://maps.googleapis.com/maps/api/geocode/json?address=%s" % urllib.quote(data["address"]+data["country"])
			response = urllib2.urlopen(grequest)
			geocode = response.read() #convert into json object extract lat and lng then save them to server with Destination object
			geocode = json.loads(geocode)
			#print(geocode['results'][0]['formatted_address'])
			#print(geocode['results'][0]['geometry']['location'])	
			dest = Destination(num, geocode['results'][0]['formatted_address'], data['country'], geocode['results'][0]['geometry']['location']['lat'], geocode['results'][0]['geometry']['location']['lng'], True)
			print(data) 
			if(data['preference'] == 'email'):
				host = Contact(new, data["host"], data["address"],data["email"],data["country"],0,num,2)

			elif(data['preference'] == 'phone'):
				host = Contact(new, data["host"], data["address"],'',data["country"],data["phone"],num,1)

			elif(data['preference'] == 'mail'):
				host = Contact(new, data["host"], data["address"],'',data["country"],0,num,3)

			#host = Contact(data["host"], data["address"],'',data["country"],'','',data["preference"])
			host.save() 
			dest.save() 	
			#return a thank you alert and then send them to index to see the location added to the map!
			#need to also verify with captchas 
			coordinates = collect_coordinates()
			messages.add_message(request, messages.INFO, 'Thanks! We will contact you once we find a way there! ') 
			#re-route to thank you page
			return render(request, "index.html", {'coordinates' : coordinates })
		else:
			return render(request, "experience.html", {'form': form})
	else:
		return render(request, "experience.html", {'form': form}) #form may be wrong but render info and then form underneath

		
		
def donate(request):
	# render all donations front for organizations/NGOs/Nonprofits
	# have top parts for us and specific donations request(specifically goes to us and then we do what they ask) 
	# have urls to donate directly 
	return render(request, "donate.html") #may have to do forms to do donations or set up gofund me or something

def about(request):
	#simple about with introduction video 
	return render(request, "thanks.html"); 
	

def contact(request):
	#sends us email
	return render(request, "contactus.html", {'form': form})

def donate(request):
	#page to donate with bitcoin or paypal
	return render(request, "thanks.html") 	

def pics(request):
	#list all pictures by country
	return render(request, "thanks.html") 	

def vlogs(request):
	#list all vlogs by country
	blogs = Blog.objects.all() 
	return render(request, "blog.html", {'blogs': blogs}) 	
	
def thanks(request):
	#static thank you page
	return render(request, "thanks.html") 
