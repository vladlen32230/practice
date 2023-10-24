//task 1

function getAge(birthYear) {
    currentYear=new Date().getFullYear();
    return currentYear-birthYear;
}

console.log(getAge(1998));
console.log(getAge(1991));
console.log(getAge(2007));

//task 2

function filter(whiteList, blackList) {
    let filteredEmails=[];
    let blackListAsSet=new Set(blackList);
    for (let email of whiteList) {
        if (!blackListAsSet.has(email)) {
            filteredEmails.push(email);
        }
    }

    return filteredEmails;
}

console.log(filter(['my-email@gmail.ru', 'jsfunc@mail.ru', 'annavkmail@vk.ru', 'fullname@skill.ru', 'goodday@day.ru'], ['jsfunc@mail.ru','goodday@day.ru']));

//task 3

function arrSort(array) {
    for (let limit=array.length; limit>0; limit--) {
        for (let left=0; left<=limit-1; left++) {
            if (array[left]>array[left+1]) {
                temp=array[left+1];
                array[left+1]=array[left];
                array[left]=temp;
            }
        }
    }

    return array;
}

console.log(arrSort([2,5,1,3,4]));
console.log(arrSort([12,33,3,44,100]));
console.log(arrSort([0,1]));