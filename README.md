# trektheplanet
Website Map Overlay for TrekThePlanet website


Written using jQuery, Bootstrap, Google-maps API and hopefully Django Python! 


This website will track and log the travels and expenses of TechnoHippy and CyberPunk
Be able to click on a site we are at or going to visit to see information on the trip and 
a video diary listing from both of us. Along with highlight videoes. 

The site will allow people to donate to us and/or offer advice. 

Probably will add facebook functionality or sometype of commenting system to be able to talk to visitors. 


To get started: 

SHOWN HOW TO IN LINUX

start up the virtual enviroment: 

source ./env/bin/activate 

INSTALL PYTHON DEPENDENCIES: 

pip install requirements.txt 
   - don't use sudo or you will be installing dependencies to your computer and not the virtual enviroment

Make migrations and create superuser: 

	python manage.py makemirgrations 
	python manage.py migrate
	python manage.py createsuperuser
		-follow any prompts 


Run the server: 
	python manage.py runserver


