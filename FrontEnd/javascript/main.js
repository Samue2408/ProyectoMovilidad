const placeInput = document.getElementById("place-input");
let map;
let autocomplete;
let properties = [
  {
    id: 1,
    nombre: "universidad libre centro",
    telefono: 11111111,
    coords: {
      lat: 10.988737604812494,
      lng: -74.78812772149456,
    },
    cuartos: "3",
    banios: "2",
    direccion: "Calle Mazatlán 222",
    ciudad: "Ciudad de México",
  },
];

window.initMap = function () {
  firstPositionMap();
  let infoWindow = new google.maps.InfoWindow();
  const addMarker = (properties) => {
    properties.forEach((propertie) => {
      const informationCard = createInfoWindow(propertie);
      const marker = new google.maps.Marker({
        position: propertie.coords,
        map,
        icon: ".././img/marker.png",
      });
      google.maps.event.addListener(marker, "click", () => {
        infoWindow.setContent(informationCard);
        infoWindow.open(map, marker);
        map.setCenter(propertie.coords);
        map.setZoom(40);
      });
    });
  };
  getYourApproximateLocation();
  addMarker(properties);
  searchGoogleMap();
};

const searchGoogleMap = () => {
  autocomplete = new google.maps.places.Autocomplete(placeInput);
  autocomplete.addListener("place_changed", () => {
    if (placeInput.value !== "") {
      const place = autocomplete.getPlace();
      map.setCenter(place.geometry.location);
      map.setZoom(40);
    }
  });
};
const firstPositionMap = () => {
  const coords = { lat: 11.004696200585443, lng: -74.80463317571127 };
  map = new google.maps.Map(document.getElementById("map"), {
    zoom: 40,
    center: coords,
  });
};

const createInfoWindow = (propertie) => {
  return `
  <div>
    <h3 class="text-reset py-1">${propertie.nombre}</h3>
    <div class="d-flex justify-content-space-between">
      <p><b>Cuartos: </b>${propertie.cuartos}</p>
      <p><b>Baños: </b>${propertie.banios}</p>
    </div>
    <p><b>Teléfono: </b>${propertie.telefono}</p>
  </div>
  `;
};
const getYourApproximateLocation = () => {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      ({ coords: { latitude, longitude } }) => {
        const coords = {
          lat: latitude,
          lng: longitude,
        };
        map.setCenter(coords);
        map.setZoom(40);
        new google.maps.Marker({
          position: coords,
          map: map,
          icon: ".././img/position.svg",
        });
      },
      () => {
        alert(
          "Tu navegador esta bien, pero ocurrio un error al obtener tu ubicación"
        );
      }
    );
  } else {
    alert("Tu navegador no cuenta con localizacion ");
  }
};
