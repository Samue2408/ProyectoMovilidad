// Obtener el formulario y los campos de entrada
const updateForm = document.getElementById("update-form");
const nombreInput = document.getElementById("nombre");
const contrasenaInput = document.getElementById("contrasena");

// Agregar un evento de envío al formulario
updateForm.addEventListener("submit", function(event) {
    event.preventDefault(); // Evitar la recarga de la página por defecto

    // Obtener los valores de los campos
    const nuevoNombre = document.getElementById("nombre").value;
    const nuevaContrasena = document.getElementById("contrasena").value;
    const nuevoEmail = document.getElementById("email").value;
    const nuevoGenre = document.getElementById("genre").value;

    // Crear un objeto con los datos a enviar a la API
    const data = {
        id_user: user_id, // Supongamos que tienes una variable user_id definida
        name: nuevoNombre,
        password: nuevaContrasena,
        email: nuevoEmail,
        genre: nuevoGenre,
    };

    // Realizar la solicitud PUT a la API
    fetch('/updateuser', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.text())
    .then(responseText => {
        // Manejar la respuesta de la API, por ejemplo, mostrar un mensaje de éxito
        alert(responseText);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});