function createStudentsList(students) {
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
}