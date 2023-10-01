// first task

let x1 = 2;
let y1 = 3;

let x2 = 10;
let y2 = 5;

console.log(Math.abs((x2-x1)*(y2-y1)));

x1 = 10;
y1 = 5;

x2 = 2;
y2 = 3;

console.log(Math.abs((x2-x1)*(y2-y1)));

x1 = -5;
y1 = 8;

x2 = 10;
y2 = 5;

console.log(Math.abs((x2-x1)*(y2-y1)));

x1 = 5;
y1 = 8;

x2 = 5;
y2 = 5;

console.log(Math.abs((x2-x1)*(y2-y1)));

x1 = 8;
y1 = 1;

x2 = 5;
y2 = 1;

console.log(Math.abs((x2-x1)*(y2-y1)));

// task 2

let fractionA = Math.floor((13.123456789 % 1) * Math.pow(10, 5));
let fractionB = Math.floor((2.123 % 1) * Math.pow(10, 5));

console.log(fractionA);
console.log(fractionB);
console.log(fractionA > fractionB);
console.log(fractionA < fractionB);
console.log(fractionA >= fractionB);
console.log(fractionA <= fractionB);
console.log(fractionA === fractionB);
console.log(fractionA !== fractionB);

fractionA = Math.floor((13.890123 % 1) * Math.pow(10, 2));
fractionB = Math.floor((2.891564 % 1) * Math.pow(10, 2));

console.log(fractionA);
console.log(fractionB);
console.log(fractionA > fractionB);
console.log(fractionA < fractionB);
console.log(fractionA >= fractionB);
console.log(fractionA <= fractionB);
console.log(fractionA === fractionB);
console.log(fractionA !== fractionB);

fractionA = Math.floor((13.890123 % 1) * Math.pow(10, 3));
fractionB = Math.floor((2.891564 % 1) * Math.pow(10, 3));

console.log(fractionA);
console.log(fractionB);
console.log(fractionA > fractionB);
console.log(fractionA < fractionB);
console.log(fractionA >= fractionB);
console.log(fractionA <= fractionB);
console.log(fractionA === fractionB);
console.log(fractionA !== fractionB);

// task 3

let rand = function(n, m) {
    let range = Math.abs(n - m);
    return Math.round(range * Math.random() + Math.min(n, m));
}

console.log(rand(0, 100));
console.log(rand(2, 5));
console.log(rand(100, -5));
console.log(rand(-3, -10));