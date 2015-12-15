	var map;
	var countries = {};
	var counter = 0; // number of countries
	function sortByCountry(x, y){
		return ((x.fields.country == y.fields.country) ? 0 : ((x.fields.country > y.fields.country) ? 1 : -1 ));
	}
	function country_assignment(){
		while(coordinates.length){
			var c = coordinates.shift(),
			    f = c.fields.country; 
			(countries[f] = countries[f] || []).push(c); 
		}	
		console.log(countries);

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
		country_assignment();
		for(c in countries){
		//	console.log("in country: "); 
		//	console.log(c); 
		//	console.log("creating everything for location: ")
		//	console.log(countries[c]);
			for(d in countries[c]){
				var contentStr = '<div class=\"info\"> ' + '<p>' + countries[c][d].fields.country +'</p></div>';   
					var infoWindow = new google.maps.InfoWindow({
					content: contentStr
				});
				var marker = new google.maps.Marker({
					position: new google.maps.LatLng(countries[c][d].fields.latitude, countries[c][d].fields.longitude),
					map:map,
					title:countries[c][d].fields.country,
					id: (counter++)  //need to make special ids for them 
				});
			
				markers.push(marker);
				infoWindows.push(infoWindow); 			
			//if the nodes are in the same country take the first node then map it to the other nodes (only taking first node for now) 
				

			//path.push(new google.maps.LatLng(coordinates[i].fields.latitude, coordinates[i].fields.longitude));
			//end of for loop making the infowindows and plotting markers
		 
		for(j = 0; j < markers.length; j++){
			var counter = j;
			markers[j].addListener('click', function(){
				infoWindows[this.id].open(map, markers[this.id]);
				console.log(counter);
			});
		}//end of creating listeners for markers

		//you can pick a home country
		//you  can pick cities to leave from and where to 
		//can also compute the paths
		paths = [];
		for(k in countries){
			base = {lat: countries[k][0].fields.latitude, lng: countries[k][0].fields.longitude};  
			for(e in countries[k]){
			//	base = {lat: countries[k][0].fields.latitude, lng: countries[k][0].fields.longitude};  
				ps2 = {lat: countries[k][e].fields.latitude, lng: countries[k][e].fields.longitude}; 
				var path = new google.maps.Polyline({
					path: [base, ps2], 
					geodesic: true, 
					strokeColor: '#FF0000',
					strokeOpacity:1.0, 
					strokeWeight: 1
				});		 
				path.setMap(map); 	
			}//end of e 

		}//end of k in countries 
		//need a listener for button to choose best/cheapest path across
		//connect by cost, connect if int'l airport, connect if on destination path
		//make path that is if have saved destination path. make form for it, and take each coordinate and either create one or take an existing one and add it to the map

	}
				
	
			
}//end of initMap

}
 
	// Resize stuff...
	google.maps.event.addDomListener(window, "resize", function() {
	   var center = map.getCenter();
	   google.maps.event.trigger(map, "resize");
	   map.setCenter(center); 
	});
	
