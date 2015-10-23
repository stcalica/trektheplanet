	var map;
	function initMap() {
		map = new google.maps.Map(document.getElementById('trek-map'), {
			center: {lat: 9.7500, lng: 100.0333},
			zoom: 2
		});
		
		var coors1 = $.parseJSON($(".coordinates")[0].val())
		var coors2 = $.parseJSON($(".coordinates")[1].val())

		var c1 = new google.maps.LatLng(coors1["lat"], coors1["lng"]);		
		var c2 = new google.maps.LatLng(coors2["lat"], coors2["lng"]);		

		var markers = new google.maps.Marker({
			position: c1,
			map: map,
		});
		
	
		var markers = new google.maps.Marker({
		position: c2,
		map: map,
		});
			
			

	}
	// Resize stuff...
	google.maps.event.addDomListener(window, "resize", function() {
	   var center = map.getCenter();
	   google.maps.event.trigger(map, "resize");
	   map.setCenter(center); 
	});
	
function addMarker(location){
		//adds marker to map at initMap
		//accepts google.maps.LatLng objects

}	

function initMakers(){
	//initialize all markers on the map 


}

function initPaths(){
	//initialize all paths



}

function currentPos(){
	//marker bounces at current position along with new icons(our faces?) 


}