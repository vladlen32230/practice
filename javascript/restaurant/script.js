const cards = document.querySelector('.cards');

window.onload = async () => {
    const menu = await fetch('db.json').then(resp => resp.json());

    menu.forEach(element => {
        let card = make_card(element);
        cards.append(card);
    });
}

function make_card(dish) {

}