// Obtener el formulario y los campos de entrada
const updateForm = document.getElementById("guardar_info");
const nombreInput = document.getElementById("nombre");
const contrasenaInput = document.getElementById("contrasena");





// Agregar un evento de envío al formulario
updateForm.addEventListener("click", function(event) {
    event.preventDefault(); // Evitar la recarga de la página por defecto

    // Obtener los valores de los campos
    const nuevoNombre = document.getElementById("inputName").value;
    const nuevoEmail = document.getElementById("inputEmail4").value;
    const nuevoPassword = document.getElementById("inputPassword4").value;
    const id = document.getElementById("id_user").value

    // Crear un objeto con los datos a enviar a la API
    const data = {
        name: nuevoNombre,
        password: nuevoPassword,
        id_user: id
    };

    // Realizar la solicitud PUT a la API
    fetch('/api/updateuser', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.text())
    .then(responseText => {
        // Manejar la respuesta de la API, por ejemplo, mostrar un mensaje de éxito
        alert("Datos guardados");
    })
    .catch(error => {
        console.error('Error:', error);
    });
});