const api = {
    base: 'https://api.openweathermap.org/data/2.5/',
    key: 'dsafsg6df8g55sa4gsa5a8s5f98sdafj'
}

const dateBuilder = (d) => {
    const months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ];

    const days = [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
    ];

    const day = days[d.getDay()];
    const date = d.getDate();
    const month = months[d.getMonth()];
    const year = d.getFullYear();

    return `${day} ${date} ${month} ${year}`;
}

const input = document.querySelector('.searchbar');
const container = document.querySelector('.location-container');

let store = {};
let city = 'London';

input.addEventListener('keyup', (e) => {
    if (e.key == 'Enter' && e.target.value) {
        city = e.target.value;
        fetchdata();
        e.target.value = '';
    }
});

const fetchdata = async () => {
    const response = await fetch(`${api.base}weather?q=${city}&appid=${api.key}`).then(res => res.json());
    const {name, weather, main: {temp}, sys: {country}} = response;
    store = {
        name,
        weather: weather[0].main,
        temp, 
        country
    };

    renderComponent();
}

const renderComponent = () => {
    container.innerHTML = getContent();
}

const getContent = () => {

    const {name, weather, temp, country} = store;

    return `<div class="location-box">
    <div class="location">
        ${name}, ${country}
    </div>
    <div class="date">
        ${dateBuilder(new Date())}
    </div>
</div>

<div class="weather-box">
    <div class="temp">
        ${temp}
    </div>
    <div class="weather">
        ${weather}
    </div>
</div>`
}