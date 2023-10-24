button=document.createElement('button');
button.textContent='Показать список';
document.body.append(button);

button.addEventListener('click', function() {
    let students=[
        {name: 'Валя', age: 11},
        {name: 'Таня',age: 24},
        {name: 'Рома',age: 21},
        {name: 'Надя', age: 34},
        {name: 'Антон', age: 7}
       ]
    let ul=document.createElement('ul');
    for (let student of students) {
        let li=document.createElement('li');
        li.style.border='2px solid black';
        let h=document.createElement('h2');
        h.textContent=student.name;
        let span=document.createElement('span');
        span.textContent=student.age;
        li.append(h, span);
        ul.append(li);
    }

    document.body.append(ul);
    button.style.display='none';
});