class MyMenu extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: "open" });

    const template = document.createElement("template");

    template.innerHTML = `
        <style>
          
        .nav-bg {
          background-color: var(--secundario);
        }
        .navegacion-principal {
          display: flex;
          flex-direction: column;
        }
        @media (min-width: 480px) {
          .navegacion-principal {
            flex-direction: row;
            justify-content: space-between;
          }
        }
        .navegacion-principal a {
          padding: 1rem;
          color: var(--blanco);
          text-decoration: none;
          font-size: 2rem;
          font-weight: 700;
        }
        .navegacion-principal a:hover {
          background-color: var(--primario);
          color: var(--blanco);
        }
        .imag {
          width: 10%;
        }
        </style>
        <div class="nav-bg">
          <img class="imag" src=".././img/bisi.png" />
          <nav class="navegacion-principal contenedor">
            <a href="index.html">Pagina principal</a>
            <a href="mapa.html">Mapa</a>
            <a href="foro.html">Comunidad</a>
            <a href="#">Contacto</a>
            <a href="ciclorutas.html">Ciclorutas</a>
            <a href="login.html">Iniciar Sesion</a>
          </nav>
        </div>
      `;

    this.shadowRoot.appendChild(template.content.cloneNode(true));
  }
}

customElements.define("my-menu", MyMenu);
