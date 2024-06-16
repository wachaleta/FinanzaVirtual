class SubcuentaButton extends HTMLElement {
    constructor() {
        super();
        const shadow = this.attachShadow({ mode: 'open' });

        const subcuenta = document.createElement('div');
        subcuenta.className = "Subcuenta"

        const titulo = document.createElement('p');
        titulo.textContent = this.getAttribute('nombre') + " - Q" + this.getAttribute("saldo");

        subcuenta.appendChild(titulo);
        shadow.appendChild(subcuenta);
    }
}

customElements.define('subcuenta-button', SubcuentaButton);