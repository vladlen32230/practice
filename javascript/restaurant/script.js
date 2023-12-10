const cards = document.querySelector('.cards');
const nameSearch = document.querySelector('.name-search');
const categorySelect = document.querySelector('.category-select');
const priceSelect = document.querySelector('.price-select');
const cartHeader = document.querySelector('.cart-header');
const cart = document.querySelector('.cart');
const closeCart = document.querySelector('.cart-close');
const cartTable = document.querySelector('.cart-table');
const sum = document.querySelector('.sum');

let menu;
let filterTimer;

async function load_menu() {
    filteredMenu = menu
    .filter(dish => dish.name.toLowerCase().includes(nameSearch.value.toLowerCase()) 
    && (dish.category == categorySelect.value || categorySelect.value == ''))
    .sort((first, second) => (first.price - second.price) * priceSelect.value);

    cards.innerHTML = '';

    filteredMenu.forEach(dish => {
        const card = make_card(dish);
        cards.append(card[0], card[1]);
    });
}

function make_card(dish) {
    const card = document.createElement('div');
    card.className = 'dish';
    card.dataset.cardId = dish.id;

    const img = document.createElement('img');
    img.className = 'dish-image';
    img.src = dish.img;
    card.append(img);

    const name = document.createElement('h3');
    name.className = 'dish-name';
    name.textContent = dish.name;
    card.append(name);

    const price = document.createElement('p');
    price.textContent = dish.price + ' Рублей';
    card.append(price);

    const add = document.createElement('button');
    add.className = 'add';
    add.textContent = 'В корзину';
    add.addEventListener('click', () => addToCart(dish));
    card.append(add);

    const extended_card = make_extended_card(dish);
    card.append(extended_card);

    card.addEventListener('click', (e) => {
        if (!e.target.closest('.add')) {
            extended_card.hidden = false;
        }
    });

    return [card, extended_card];
}

function make_extended_card(dish) {
    const extendedCard = document.createElement('div');
    extendedCard.className = 'extended-card';
    extendedCard.hidden = true;
    extendedCard.id = dish.id;

    const close = document.createElement('img');
    close.className = 'close';
    close.src = 'img/cross.png';
    close.addEventListener('click', () => extendedCard.hidden = true);

    extendedCard.append(close);

    const img = document.createElement('img');
    img.className = 'extended-dish-image';
    img.src = dish.img;
    extendedCard.append(img);

    const name = document.createElement('h3');
    name.className = 'dish-name';
    name.textContent = dish.name;
    extendedCard.append(name);

    const category = document.createElement('p');
    category.innerHTML = 'Категория: ' + `<strong>${dish.category}</strong>`;
    extendedCard.append(category);

    const ingredients = document.createElement('p');
    ingredients.innerHTML = 'Ингредиенты: ' + `<strong>${dish.ingredients.join(', ')}</strong>`;
    extendedCard.append(ingredients);

    const mass = document.createElement('p');
    mass.innerHTML = 'Масса: ' + `<strong>${dish.mass + ' грамм'}</strong>`;
    extendedCard.append(mass);

    const price = document.createElement('p');
    price.innerHTML = 'Цена: ' + `<strong>${dish.price + ' рублей'}</strong>`;
    extendedCard.append(price);

    const add = document.createElement('button');
    add.className = 'add'
    add.textContent = 'В корзину';
    add.addEventListener('click', () => addToCart(dish));
    extendedCard.append(add);

    return extendedCard;
}

window.onload = async () => {
    menu = await fetch('db.json').then(resp => resp.json());
    closeCart.addEventListener('click', () => cart.hidden = true);
    load_menu();
};

[nameSearch, categorySelect, priceSelect].forEach(filter => {
    filter.addEventListener('input', () => {
        clearTimeout(filterTimer);
        filterTimer = setTimeout(load_menu, 1000);
    });
});

function addToCart(dish) {
    let currentDish = JSON.parse(window.localStorage.getItem(dish.id));

    if (currentDish) {
        currentDish.quantity += 1;
        window.localStorage.setItem(dish.id, JSON.stringify(currentDish));
    } else {
        window.localStorage.setItem(dish.id, JSON.stringify({'name': dish.name, 'quantity': 1, 'price': dish.price}));
    }
}

cartHeader.addEventListener('click', () => {
    renderCart();
    cart.hidden = false;
});

function renderCart() {
    cartTable.innerHTML = 
    `
    <th>Название</th>
    <th>Количество</th>
    <th>Стоимость</th>
    <th>Удалить</th>
    `;

    let sumPrice = 0;
    Object.entries(window.localStorage).forEach(entry => {
        const id = parseInt(entry[0]);
        const dish = JSON.parse(entry[1]);

        const row = document.createElement('tr');

        const name = document.createElement('td');
        name.textContent = dish.name;
        row.append(name);

        const quantity = document.createElement('td');
        quantity.textContent = dish.quantity;
        row.append(quantity);

        const price = document.createElement('td');
        price.textContent = `${dish.price * dish.quantity}`;
        row.append(price);

        sumPrice += dish.price * dish.quantity;

        const remove = document.createElement('td');
        const img = document.createElement('img');
        img.className = 'remove-dish'
        img.src = 'img/cross.png';
        img.addEventListener('click', () => {
            window.localStorage.removeItem(id);
            renderCart();
        });

        remove.append(img);
        row.append(remove);

        cartTable.append(row);
    });

    sum.textContent = `Итого: ${sumPrice} рублей`;
}