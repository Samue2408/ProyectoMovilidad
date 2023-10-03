function enviarMensaje() {
  var comunidadSelector = document.getElementById("comunidadSelector");
  var comunidadSeleccionada = comunidadSelector.value;
  var mensaje = document.getElementById("message").value;

  if (mensaje.trim() !== "") {
    var mensajeHtml =
      "<div class='message'><strong>Usuario:</strong> " + mensaje + "</div>";
    document.getElementById(comunidadSeleccionada).innerHTML += mensajeHtml;
    document.getElementById("message").value = "";
  }
}
