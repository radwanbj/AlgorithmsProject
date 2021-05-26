function initMap() {
    const directionsService = new google.maps.DirectionsService();
    const directionsRenderer = new google.maps.DirectionsRenderer();
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 7,
      center: { lat: 3.1000170516638885,lng: 101.53071480907951 },
    });
    directionsRenderer.setMap(map);
  
    console.log("radwan")

    calculateAndDisplayRoute(directionsService, directionsRenderer);
      //document.getElementById("start").addEventListener("change", onChangeHandler);
    //document.getElementById("end").addEventListener("change", onChangeHandler);
  }
  
  function calculateAndDisplayRoute(directionsService, directionsRenderer) {
    directionsService.route(
      {
        origin: {
          query: '3.3615395462207878,101.56318183511695'
        },
        destination: {
          query: '3.1000170516638885,101.53071480907951'
        },
        waypoints: [
            {
          location: '3.112924170027219, 101.63982650389863',
          stopover: true,
        }
        ],
        travelMode: google.maps.TravelMode.DRIVING,
      },
      (response, status) => {
        if (status === "OK") {
          directionsRenderer.setDirections(response);
        } else {
          window.alert("Directions request failed due to " + status);
        }
      }
    );
  }
  