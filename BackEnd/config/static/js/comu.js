document.getElementById("publi").addEventListener("click", function (event) {
  const menssage = document.getElementById("mensaje").value;
  const user = document.getElementById("id_user").value;
  const com = document.getElementById("id_com").value;

  const userData = {
    id_com: com,
    id_user: user,
    menssage: menssage,
  };

  fetch("/api/savepublication", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(userData),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.error) {
        Swal.fire({
          title: data.error,
          text: "Credenciales incorrectas",
          footer:
            '<p>Si has <a href="/hidden_pw">olvidado tu contraseña</a>, puedes restablecerla</p>',
          icon: "error",
          backdrop: false,
          timer: 7000,
          timerProgressBar: true,
        });
      } else {
        Swal.fire({
          title: data.mensaje,
          text: "Inicio de sesión exitoso",
          icon: "success",
          backdrop: false,
          timer: 3500,
        }).then((result) => {});
      }
      window.location.reload();
    })
    .catch((error) => console.error(error));
});
