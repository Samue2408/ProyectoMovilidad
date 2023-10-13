function initMap() {
  const directionsRenderer = new google.maps.DirectionsRenderer();
  const directionsService = new google.maps.DirectionsService();
  let map;

  // Obtener la ubicación del usuario
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        const userLocation = {
          lat: position.coords.latitude,
          lng: position.coords.longitude,
        };

        // Crear el mapa centrado en la ubicación del usuario
        map = new google.maps.Map(document.getElementById("map"), {
          zoom: 14,
          center: userLocation,
        });

        directionsRenderer.setMap(map);

        // Crear un marcador en la ubicación del usuario con tamaño personalizado
        new google.maps.Marker({
          position: userLocation,
          map: map,
          icon: {
            url: "{{url_for('static', filename='../img/bisi.png')}}", // Ruta a tu icono de marcador
            scaledSize: new google.maps.Size(32, 32), // Tamaño personalizado del icono
          },
          title: "Tu ubicación",
        });

        // Inicializar el objeto de autocompletar para el campo de origen
        const fromInput = document.getElementById("from");
        const fromAutocomplete = new google.maps.places.Autocomplete(fromInput);

        // Inicializar el objeto de autocompletar para el campo de destino
        const toInput = document.getElementById("to");
        const toAutocomplete = new google.maps.places.Autocomplete(toInput);

        fromAutocomplete.addListener("place_changed", function () {
          const place = fromAutocomplete.getPlace();
          if (!place.geometry) {
            window.alert(
              "No details available for input: '" + place.name + "'"
            );
            return;
          }

          const selectedLocation = {
            lat: place.geometry.location.lat(),
            lng: place.geometry.location.lng(),
          };

          calculateAndDisplayRoute(
            directionsService,
            directionsRenderer,
            selectedLocation
          );
        });

        toAutocomplete.addListener("place_changed", function () {
          const place = toAutocomplete.getPlace();
          if (!place.geometry) {
            window.alert(
              "No details available for input: '" + place.name + "'"
            );
            return;
          }

          const selectedLocation = {
            lat: place.geometry.location.lat(),
            lng: place.geometry.location.lng(),
          };

          calculateAndDisplayRoute(
            directionsService,
            directionsRenderer,
            selectedLocation
          );
        });

        document.getElementById("mode").addEventListener("change", () => {
          calculateAndDisplayRoute(directionsService, directionsRenderer);
        });

        // Calcular y mostrar la ruta inicial desde la ubicación del usuario
        calculateAndDisplayRoute(
          directionsService,
          directionsRenderer,
          userLocation
        );
      },
      () => {
        alert("Error al obtener la ubicación del usuario.");
      }
    );
  } else {
    alert("Tu navegador no soporta geolocalización.");
  }
}

function calculateAndDisplayRoute(
  directionsService,
  directionsRenderer,
  selectedLocation
) {
  const selectedMode = document.getElementById("mode").value;
  const origin = selectedLocation || document.getElementById("from").value;
  const destination = document.getElementById("to").value;

  directionsService
    .route({
      origin: origin,
      destination: destination,
      travelMode: google.maps.TravelMode[selectedMode],
    })
    .then((response) => {
      directionsRenderer.setDirections(response);
    })
    .catch((e) => window.alert("Error al calcular la ruta: " + e.status));
}
