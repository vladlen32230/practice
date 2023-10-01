// task 1

let passwordCorrect1 = '1234-';
let passwordCorrect2 = '1234-';
let passwordCorrect3 = 'qaz-xsw';
let passwordCorrect4 = '_zxd';

let passwordIncorrect1 = '_-a';
let passwordIncorrect2 = 'qaz';
let passwordIncorrect3 = '_-3';
let passwordIncorrect4 = '123456789';

let check = function(password) {
    if (password.length >= 4 && (password.includes('-') || password.includes('_'))) {
        return 'Пароль надежный';
    } else {
        return 'Пароль недостаточно надежный';
    }
}

console.log(check(passwordCorrect1));
console.log(check(passwordCorrect2));
console.log(check(passwordCorrect3));
console.log(check(passwordCorrect4));

console.log(check(passwordIncorrect1));
console.log(check(passwordIncorrect2));
console.log(check(passwordIncorrect3));
console.log(check(passwordIncorrect4));

// task 3

let validate = function(name, surname) {
    let validatedName = name.substring(0, 1).toUpperCase() + name.substring(1).toLowerCase();
    let validatedSurname = surname.substring(0, 1).toUpperCase() + surname.substring(1).toLowerCase();
    console.log(validatedName);
    console.log(validatedSurname);
    console.log(validatedName !== name ? 'Имя было преобразовано' : 'Имя осталось без изменений');
    console.log(validatedSurname !== surname ? 'Фамилия была преобразована' : 'Фамилия осталась без изменений');
}

validate('Vlad', 'Kudrin');
validate('sereGA', 'Pirate');
validate('_)_$', '%^&*');
validate('my', 'bike');
validate('ON', 'MOON');

// task 3

let isEven = function(number) {
    if (number % 2 === 0 && number !== 0) {
        return true;
    }

    return false;
}

console.log(isEven(1));
console.log(isEven(2));
console.log(isEven(10));
console.log(isEven(2.5));
console.log(isEven(-4));
console.log(isEven(0));
console.log(isEven(-3.8));