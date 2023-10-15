const container = document.getElementById("container");
const registerBtn = document.getElementById("register");
const loginBtn = document.getElementById("login");

// Obtener el formulario y los campos de entrada

const nombreInput = document.getElementById("nombre");
const contrasenaInput = document.getElementById("contrasena");

registerBtn.addEventListener("click", () => {
  container.classList.add("active");
});

loginBtn.addEventListener("click", () => {
  container.classList.remove("active");
});

document.getElementById("signup").addEventListener("click", function (event) {

  const name = document.getElementById('name_r').value;
  const email = document.getElementById('email_r').value;
  const password = document.getElementById('password_r').value;
  const genre = document.getElementById('genre_r').value;

  if (name.trim() === '' || email.trim() === '' || password.trim() === '') {    
    alert('Por favor, completa todos los campos y/o selecciona un género.');
  } else if (genre.trim() === '') {    
    alert('Por favor, selecciona un género.');
  } else {    
    const dataToSend = {
      name: name,
      email: email,
      password: password,
      genre: genre
    };
    fetch('/api/saveuser', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(dataToSend)
    }) 
    .then(response => response.json())  
    .then(data => {
      if (data.error) {
        Swal.fire({
          title: data.error
        })
      } else {
        alert(data.mensaje)
        window.location.href = "/login";       
      }            
    })
    .catch(error => console.error(error));
  }  
  event.preventDefault();
}); 

document.getElementById("signin").addEventListener("click", function (event) {
  event.preventDefault();
  const email = document.getElementById('email_l').value;
  const password = document.getElementById('password_l').value;

  const userData = {
    email: email,
    password: password
  };

  fetch('/api/signin', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(userData)
  })
    .then(response => response.json())
    .then(data => {
      if (data.error) {
        alert('error')
      } else {
        alert('Succesfull')    
        window.location.href = "/";       
      }            
    })
    .catch(error => console.error(error));
          
});

// Obtener el formulario y los campos de entrada
const updateForm = document.getElementById("update-form");

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
