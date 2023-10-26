// Этап 1. В HTML файле создайте верстку элементов, которые будут статичны(неизменны).

// Этап 2. Создайте массив объектов студентов.Добавьте в него объекты студентов, например 5 студентов.

let studentsList;

// Этап 3. Создайте функцию вывода одного студента в таблицу, по аналогии с тем, как вы делали вывод одного дела в модуле 8. Функция должна вернуть html элемент с информацией и пользователе.У функции должен быть один аргумент - объект студента.

function getStudentItem(studentObj) {
    const row=document.createElement('tr');

    const surname=document.createElement('td');
    surname.textContent=studentObj.surname;
    row.append(surname);

    const name=document.createElement('td');
    name.textContent=studentObj.name;
    row.append(name);

    const middlename=document.createElement('td');
    middlename.textContent=studentObj.middlename;
    row.append(middlename);

    const faculty=document.createElement('td');
    faculty.textContent=studentObj.faculty;
    row.append(faculty);

    const birthdate=document.createElement('td');
    birthdate.textContent=`${new Date(Date.parse(studentObj.birthdate)).toISOString().split('T')[0]} (${(new Date().getFullYear()-new Date(Date.parse(studentObj.birthdate)).getFullYear())} лет)`;
    row.append(birthdate);

    const span=document.createElement('td');
    const difference=new Date().getFullYear()-studentObj.startDate
    span.textContent=`${studentObj.startDate}-${studentObj.startDate+4} (${difference>4?'Закончил':difference+1+' курс'})`;
    row.append(span);

    const deleteColumn = document.createElement('td');
    const deleteBtn = document.createElement('button');
    deleteBtn.textContent = 'Удалить';
    deleteBtn.addEventListener('click', () => deleteStudent(studentObj.id));
    deleteColumn.append(deleteBtn);
    row.append(deleteColumn);

    row.classList.add('student-row');
    row.id = 's' + studentObj.id;

    return row;
}

// Этап 4. Создайте функцию отрисовки всех студентов. Аргументом функции будет массив студентов.Функция должна использовать ранее созданную функцию создания одной записи для студента.Цикл поможет вам создать список студентов.Каждый раз при изменении списка студента вы будете вызывать эту функцию для отрисовки таблицы.

async function renderStudentsTable() {

    const students = await fetch('http://localhost:3000/students', {
        method: 'GET',
        headers: {
            'Accept': 'application/json'
        },
    }).then(res => res.json());

    studentsList = students;

    const table=document.querySelector('.students');
    Array.from(table.querySelectorAll('.student-row')).forEach(element => element.remove());
    for (let student of studentsList) {
        if (checkStudent(student)) {
            let row=getStudentItem(student);
            table.append(row);
        }
    }
}

document.addEventListener('DOMContentLoaded', renderStudentsTable);

// Этап 5. К форме добавления студента добавьте слушатель события отправки формы, в котором будет проверка введенных данных.Если проверка пройдет успешно, добавляйте объект с данными студентов в массив студентов и запустите функцию отрисовки таблицы студентов, созданную на этапе 4.

const studentForm=document.querySelector('.student-form');
studentForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const birthday=studentForm.birthday.valueAsDate;
    if (birthday<new Date('01.01.1900') || birthday>new Date()) {
        alert(`Дата рождения должна быть после 1900-01-01 и до ${new Date().toISOString().split('T')[0]}`);
        return;
    } else if (studentForm.start.value<2000 || studentForm.start.value>new Date().getFullYear()) {
        alert(`Дата поступления должна быть после 1999 и до ${new Date().getFullYear()+1}`);
        return;
    }

    const student= {
        name: studentForm.name.value.trim(),
        surname: studentForm.surname.value.trim(),
        middlename: studentForm.middlename.value.trim(),
        birthdate: studentForm.birthday.value.split('T')[0],
        faculty: studentForm.faculty.value.trim(),
        startDate: Number(studentForm.start.value),
    }

    await fetch('http://localhost:3000/students', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },

        body: JSON.stringify(student)
    });

    const students = await fetch('http://localhost:3000/students', {
        method: 'GET',
        headers: {
            'Accept': 'application/json'
        },
    }).then(res => res.json());

    studentsList = students;

    renderStudentsTable();
});

async function deleteStudent(id) {
    document.querySelector('#s' + id).remove();

    await fetch('http://localhost:3000/students/' + id, {
        method: 'delete'
    });

    renderStudentsTable();
}

// Этап 5. Создайте функцию сортировки массива студентов и добавьте события кликов на соответствующие колонки.

Array.from(document.querySelectorAll('th')).forEach(element => {
    element.addEventListener('click', () => {
        studentsList.sort((a, b)=> {
            if (a[element.getAttribute("name")]>b[element.getAttribute("name")]) return 1;
            else if (a[element.getAttribute("name")]<b[element.getAttribute("name")]) return -1;
            else return 0
        });
        
        renderStudentsTable();
    });
});

// Этап 6. Создайте функцию фильтрации массива студентов и добавьте события для элементов формы.

let typingTimer;

Array.from(document.querySelectorAll('.filter')).forEach(element => {
    element.addEventListener('input' , () => {
        clearTimeout(typingTimer);
        typingTimer=setTimeout(renderStudentsTable, 500);
    });
});

function checkStudent(student) {
    const surname=document.querySelector('#surname-filter');
    const name=document.querySelector('#name-filter');
    const middlename=document.querySelector('#middlename-filter');
    const faculty=document.querySelector('#faculty-filter');
    const start=document.querySelector('#start-year-filter');
    const end=document.querySelector('#end-year-filter');

    return student.surname.toLowerCase().includes(surname.value.toLowerCase()) && 
    student.name.toLowerCase().includes(name.value.toLowerCase()) && 
    student.middlename.toLowerCase().includes(middlename.value.toLowerCase()) && 
    student.faculty.toLowerCase().includes(faculty.value.toLowerCase()) && 
    (student.startDate==start.value || !Boolean(start.value)) && 
    (student.startDate+4==end.value || !Boolean(end.value));
}

//////////////////////////////////////


// добавление нового элемента, остальные методы (get, put, patch, delete) работаю по такой же логике

// fetch("http://localhost:3000/todos", {
//   method: "post",
//   headers: {
//     'Accept': 'application/json',
//     'Content-Type': 'application/json'
//   },
//   //make sure to serialize your JSON body
//   body: JSON.stringify({
//     id: '5',
//     text: 'do',
//     completed: true,
//     meta: {
//         author: 'dssad',
//         createdAt: 'today'
//     }
//   })
// })

// поиск сравнивает, чтобы хоть какое-то поле равнялось значению q
// fetch("http://localhost:3000/todos?q=do").then(res => res.json()).then(console.log)


// поиск по конкретному полю
//  fetch("http://localhost:3000/todos?text=Sleep").then(res => res.json()).then(console.log)

// сортировка по конкретному полю конкретным порядокм
// fetch("http://localhost:3000/todos?_sort=id&_order=desc").then(res => res.json()).then(console.log)

// поиск по id
// fetch("http://localhost:3000/todos/2").then(res => res.json()).then(console.log)

