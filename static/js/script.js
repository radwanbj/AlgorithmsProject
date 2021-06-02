$(document).ready(function () {
  $("#myForm").on('submit', function (event) {
    
    event.preventDefault();
    
    let distance = $('#distance:checked').val();
    let distanceCheck = false
    if (distance === "on"){
      distanceCheck = true
    }

    let sentiment = $('#sentiment:checked').val();
    let sentimentCheck = false
    if (sentiment === "on"){
      sentimentCheck = true
    }

    let customer = $('#customer').find(":selected").val();

      $.ajax({
          data: {
              sentiment: sentimentCheck,
              distance: distanceCheck,
              customer: customer
          },
          type: 'POST',
          url: '/'
      })
          .done(function (data) {
              if (data.error) {
                  alert(data.error);
              } else {         
                var listy = `<ol>`
                data.data.forEach(element => {
                  listy += `<li>${element[0]} ${(element[1])/1000}   km</li>`
                }); 
                console.log(data)
                listy += `</ol>`
                  $('#courierList').html(listy)
                calculateAndDisplayRoute(directionsService, directionsRenderer, data.coor, data.bestCourier)
              }
          });
  });

})


let directionsService;
let directionsRenderer;

function initMap() {
    directionsService = new google.maps.DirectionsService();
    directionsRenderer = new google.maps.DirectionsRenderer();
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 7,
      center: { lat: 3.1000170516638885,lng: 101.53071480907951 },
    });
    directionsRenderer.setMap(map);
  }
  
  function calculateAndDisplayRoute(directionsService, directionsRenderer, coor, bestCourier) {
    directionsService.route(
      {
        origin: {
          query: coor.origin
        },
        destination: {
          query: coor.destination
        },
        waypoints: [
            {
          location: bestCourier,
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
  