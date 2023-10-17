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
            url: "/static/img/bisi.png", // Ruta a tu icono de marcado
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

        const calculateRouteButton = document.getElementById("calculate-route");

        // Agregar un evento de clic al botón de calcular ruta
        calculateRouteButton.addEventListener("click", function () {
          const origin = fromInput.value;
          const destination = toInput.value;

          // Validar que ambos campos estén llenos
          if (origin && destination) {
            calculateAndDisplayRoute(
              directionsService,
              directionsRenderer,
              origin,
              destination
            );
          } else {
            // Mostrar un mensaje de error si los campos están vacíos
            window.alert(
              "Por favor, ingresa tanto el origen como el destino para calcular la ruta."
            );
          }
        });

        // Evento para el campo de origen cuando se selecciona una sugerencia del autocompletar
        fromAutocomplete.addListener("place_changed", function () {
          const place = fromAutocomplete.getPlace();
          if (!place.geometry) {
            window.alert(
              "No se encontraron detalles para el origen: " + place.name
            );
            fromInput.value = ""; // Limpiar el campo de origen si la sugerencia no es válida
          }
        });

        // Evento para el campo de destino cuando se selecciona una sugerencia del autocompletar
        toAutocomplete.addListener("place_changed", function () {
          const place = toAutocomplete.getPlace();
          if (!place.geometry) {
            window.alert(
              "No se encontraron detalles para el destino: " + place.name
            );
            toInput.value = ""; // Limpiar el campo de destino si la sugerencia no es válida
          }
        });
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
  origin,
  destination
) {
  const selectedMode = "WALKING"; // Modo de viaje: Caminar
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
