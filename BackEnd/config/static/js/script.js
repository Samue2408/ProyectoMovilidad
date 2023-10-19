const container = document.getElementById("container");
const registerBtn = document.getElementById("register");
const loginBtn = document.getElementById("login");



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
    Swal.fire({
      title: 'Faltan datos',
      text: 'Por favor, completa todos los campos',
      icon: 'error',
      backdrop: false,
      timer: 4500,
      timerProgressBar: true,
    })
  } else if (genre.trim() === '') {    
    Swal.fire({
      title: 'Faltan datos',
      text: 'Por favor, ingresa el genero',
      icon: 'error',
      backdrop: false,
      timer: 4500,
      timerProgressBar: true,
    })
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
          title: data.error,
          text: 'Ingresa otro valido',
          footer: '<p>Si ya tienes una cuenta, por favor <a href="/login">inicia sesión.</a></p>',
          icon: 'error',
          backdrop: false,
          timer: 7000,
          timerProgressBar: true,
        
          //Animacion personalizada

          //showClass: {
          //  popup: 'animate__animated animate__fadeInDown'
          //},
          //hideClass: {
          //  popup: 'animate__animated animate__fadeOutUp'
          //}
        })
      } else {
        Swal.fire({
          title: data.mensaje,
          text: 'Un gusto tenerte con nosotros',
          icon: 'success',
          backdrop: false,
          timer: 2000,
        }).then((result) => {
          window.location.href = "/login";
        });       
      }  
            
    })
    .catch(error => console.error(error));
  }  
  event.preventDefault();
}); 


document.getElementById('password_l').addEventListener("input",() => {
  const password = document.getElementById('password_l').value;
  const email = document.getElementById('email_l').value;
  const boton = document.getElementById("signin");

  if (password.trim() !== '' && email.trim() !== ''){
    
    boton.disabled = false;
  }  
  else{
    boton.disabled = true;
  }  
})

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
        Swal.fire({
          title: data.error,
          text: 'Credenciales incorrectas',
          footer: '<p>Si has <a href="/hidden_pw">olvidado tu contraseña</a>, puedes restablecerla</p>',
          icon: 'error',
          backdrop: false,
          timer: 7000,
          timerProgressBar: true,
        })
      } else {
        Swal.fire({
          title: data.mensaje,
          text: 'Inicio de sesión exitoso',
          icon: 'success',
          backdrop: false,
          timer: 3500,
        }).then((result) => {
          window.location.href = "/";
        });           
      }            
    })
    .catch(error => console.error(error));
          
});


