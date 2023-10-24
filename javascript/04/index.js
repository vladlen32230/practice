//task 1

let createRandomArray=function(m, n, count) {
    let range=Math.abs(m-n);
    let array=[]
    for (let i=0; i<count; i++) {
        let randomNumber = Math.round(Math.random()*range) + Math.min(m, n);
        array.push(randomNumber);
    }

    return array;
}

console.log(createRandomArray(0, 100, 100));
console.log(createRandomArray(2, 5, 50));
console.log(createRandomArray(100, -5, 70));
console.log(createRandomArray(-3, -10, 42));

//task 2

let createAndScrambleArray=function(count) {
    let array=[];
    for (let i=1; i<=count; i++) {
        array.push(i);
    }

    for (let i in array) {
        let j=Math.round(Math.random()*i);
        if (j!==i) {
            temp=array[i];
            array[i]=array[j];
            array[j]=temp;
        }
    }

    return array;
}
let array1=createAndScrambleArray(5);
let array2=createAndScrambleArray(7);
let array3=createAndScrambleArray(3);

console.log(array1);
console.log(array2);
console.log(array3);

//task 3

let find=function(array, num) {
    for (let i in array) {
        if (array[i]===num) {
            return true;
        }
    }

    return false;
}

console.log(find(array1, 3));
console.log(find(array2, 1));
console.log(find(array3, 7));

//task 4

let extend=function(firstArray, secondArray) {
    let extendedArray=[];
    for (let i=0; i<firstArray.length + secondArray.length; i++) {
        if (i>=firstArray.length) {
            extendedArray.push(secondArray[i-firstArray.length]);
        } else {
            extendedArray.push(firstArray[i]);
        }
    }

    return extendedArray;
}

console.log(extend([2, 2, 17, 21, 45, 12, 54, 31, 53], [12, 44, 23, 5]));