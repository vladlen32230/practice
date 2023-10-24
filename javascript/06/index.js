// task 1 and task 2

function getOlderUser(...persons) {
    if (Array.isArray(persons[0])) {
        persons=persons[0]
    }
    
    let oldestPerson=persons[0];
    for (let person of persons) {
        if (person.age>oldestPerson.age) {
            oldestPerson=person;
        }
    }

    return oldestPerson.name;
}

console.log(getOlderUser([
    {name: 'Валя', age: 11},
    {name: 'Таня',age: 24},
    {name: 'Рома',age: 21},
    {name: 'Надя', age: 34},
    {name: 'Антон', age: 7}
]));
console.log(getOlderUser(
    {name: 'Игорь',age: 17}, 
    {name: 'Оля',age: 21}
));

//task 3

function filter(objects, property, value) {
    let filteredObjects=[];
    for (let object of objects) {
        if (object[property]===value) {
            filteredObjects.push(object);
        }
    }

    return filteredObjects
}

console.log(filter([
    { name: 'Василий', surname: 'Васильев' },
    { name: 'Иван', surname: 'Иванов' },
    { name: 'Пётр', surname: 'Петров' }
],'name','Иван' ));

console.log(filter([
    { name: 'Василий', surname: 'Васильев' },
    { name: 'Иван', surname: 'Иванов' },
    { name: 'Пётр', surname: 'Петров' }
],'surname','Васильев' ));

console.log(filter([
    { name: 'Василий', surname: 'Васильев' },
    { name: 'Иван', surname: 'Иванов' },
    { name: 'Пётр', surname: 'Петров' }
],'f','Пётр' ));