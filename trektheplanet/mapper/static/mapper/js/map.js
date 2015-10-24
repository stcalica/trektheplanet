	var map;
	function initMap() {

		map = new google.maps.Map(document.getElementById('trek-map'), {
			center: {lat: 9.7500, lng: 100.0333},
			zoom: 2
		});
		var coordinates = [] 
		$(".coordinates").each(function(){

			coor = $.parseJSON($(this).val());
			console.log(coor);
			coordinates.push(coor);
			
		});
		
		var poly = new google.maps.Polyline({

			strokeColor: '#000000' , 
			strokeOpacity: 1.0 , 
			strokeWeight: 3

		});
	
		poly.setMap(map);

		for(var i =0; i < coordinates.length; i++){
			var markers = new google.maps.Marker({
				position: new google.maps.LatLng(coordinates[i].lat, coordinates[i].lng),
				map:map
			});
			
			var path = poly.getPath(); 
			path.push(new google.maps.LatLng(coordinates[i].lat, coordinates[i].lng)); 
		}
	
			
	}
	// Resize stuff...
	google.maps.event.addDomListener(window, "resize", function() {
	   var center = map.getCenter();
	   google.maps.event.trigger(map, "resize");
	   map.setCenter(center); 
	});
	
