document.getElementById("add_community").addEventListener("click", function (event) {

    event.preventDefault();

    const nombre = document.getElementById("nombre").value;
    const id = document.getElementById("id_user").value;

    const dataToSend = {
        name: nombre,
        id_user: id,
        type_usu: "lider"
    };

    fetch('/api/savecommunity', {
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
                text: 'Ingrese otro nombre para la comunidad',
                icon: 'error',
                backdrop: false,
                timer: 7000,
                timerProgressBar: true,
            })
        } else {
            return fetch('/api/saveusucom', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(dataToSend)
            });
        }
    })
    .then(response => response.json())
    .then(data => {
        
            Swal.fire({
              title: data.mensaje,
              text: 'Creacion de comunidad exitosa',
              icon: 'success',
              backdrop: false,
              timer: 3500,
            }).then((result) => {
              window.location.href = "/foro";
            });           
          
    })
    .catch (error => console.error(error));


})

