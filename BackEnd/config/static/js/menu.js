class MyMenu extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: "open" });

    const template = document.createElement("template");

    template.innerHTML = `
        <style>
        :host {
          display: block;
          width: 100%;
          position: fixed;
          top: 0;
          background-color: var(--secundario);
          z-index: 1000;
        }
        .form-container {
          margin-top: 100px; /* Ajusta este valor según sea necesario para evitar el solapamiento con el menú */
        }
        .nav-bg {
          background-color: var(--secundario);
          position: fixed;
          width: 100%; 
          z-index: 1000;
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
          <img class="imag" src="".././img/bisi.png"" />
          <nav class="navegacion-principal contenedor">
            <a href="/">Pagina principal</a>
            <a href="/mapa">Mapa</a>
            <a href="/foro">Comunidad</a>
            <a href="/#contactanos">Contacto</a>
            <a href="/ciclorutas">Ciclorutas</a>
            <a href="/login">Iniciar Sesion</a>
          </nav>
        </div>
      `;

    this.shadowRoot.appendChild(template.content.cloneNode(true));
  }
}

customElements.define("my-menu", MyMenu);
