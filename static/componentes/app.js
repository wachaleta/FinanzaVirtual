class MyCard extends HTMLElement {
    constructor() {
        super();
        const shadow = this.attachShadow({ mode: 'open' });

        const card = document.createElement('div');
        card.style.backgroundColor="red"
        card.className = 'card';

        const cardTitle = document.createElement('h2');
        cardTitle.textContent = this.getAttribute('title');

        const cardContent = document.createElement('p');
        cardContent.textContent = this.getAttribute('content');

        card.appendChild(cardTitle);
        card.appendChild(cardContent);
        shadow.appendChild(card);
    }
}

customElements.define('my-card', MyCard);