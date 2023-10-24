function createStudentCard(name, age) {
    let div=document.createElement('div');
    div.style.border='2px solid black';
    let h=document.createElement('h2');
    h.textContent=name;
    let span=document.createElement('span');
    span.textContent=age;
    div.append(h, span);
    document.body.append(div);
}