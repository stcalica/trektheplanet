	var map;
	var countries = [];
	var counter = 0; // number of countries
	function sortByCountry(x, y){
		return ((x.fields.country == y.fields.country) ? 0 : ((x.fields.country > y.fields.country) ? 1 : -1 ));
	}
	function country_assignment(){
	//assigns coordinates to a country array and then takes out coordinatse put into other arrays
	//check if matched with the new country array, if not then make new array and push into new array, if yes then push and pop!
	// to create a new array just use a for loog and new Array() 
		countries.push(new Array());
		countries[counter].push(coordinates.pop()); 
		for( var l = 0;  l < coordinates.length-1; l++){
			console.log("counter is at: ");
			console.log(counter); 
			console.log("first off of counter: ");
			console.log(countries[counter][0].fields.country); 
			console.log(countries); 
			//check if first country's array  coordinate  is equal to the next coordinate in coordinates matches with next coordinate 
			if((countries[counter][0].fields.country == coordinates[l].fields.country)){
				console.log("match!"); 
				console.log(counter); 
				console.log(coordinates[l].fields.country); 
				countries[counter].push(coordinates.pop()); 	

			} else {
				console.log("Not a match going to create anew and push in or array to be created:"); 
				console.log(coordinates[l].fields.country);
				countries.push(new Array());
				counter = counter + 1; 
			  	countries[counter].push(coordinates.pop()); 
				console.log(counter); 	
			}

		}

	}//end of country assignment
	function initMap() {

		map = new google.maps.Map(document.getElementById('trek-map'), {
			center: {lat: 9.7500, lng: 100.0333},
			zoom: 3
		});

		var poly = new google.maps.Polyline({

			strokeColor: '#000000' , 
			strokeOpacity: 1.0 , 
			strokeWeight: 3

		});
	
		poly.setMap(map);
		markers = [];
		infoWindows = [];
		paths = [];
		console.log(coordinates);
		coordinates.sort(sortByCountry);
		console.log(coordinates); 
		for(i =0; i < coordinates.length; i++){
			
			var contentStr = '<div class=\"info\"> ' + '<p>' + coordinates[i].fields.country +'</p></div>';   
			
			var infoWindow = new google.maps.InfoWindow({
				content: contentStr
			});

			var marker = new google.maps.Marker({
				position: new google.maps.LatLng(coordinates[i].fields.latitude, coordinates[i].fields.longitude),
				map:map,
				title:coordinates[i].fields.country,
				id: (coordinates[i].pk - 1)
			});
			
			markers.push(marker);
			infoWindows.push(infoWindow); 			
			//if the nodes are in the same country take the first node then map it to the other nodes (only taking first node for now) 
			country_assignment();	

		//	path.push(new google.maps.LatLng(coordinates[i].fields.latitude, coordinates[i].fields.longitude));
		}//end of for loop making the infowindows and plotting markers 
		for(j = 0; j < markers.length; j++){
			var counter = j;
			markers[j].addListener('click', function(){
				infoWindows[this.id].open(map, markers[this.id]);
				console.log(counter);
			});
		}//end of creating listeners for markers


		//grab all coordinates that have the same country
				

			
	}//end of initMap


 
	// Resize stuff...
	google.maps.event.addDomListener(window, "resize", function() {
	   var center = map.getCenter();
	   google.maps.event.trigger(map, "resize");
	   map.setCenter(center); 
	});
	
