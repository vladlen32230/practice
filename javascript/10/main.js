// Этап 1. В HTML файле создайте верстку элементов, которые будут статичны(неизменны).

// Этап 2. Создайте массив объектов студентов.Добавьте в него объекты студентов, например 5 студентов.

const studentsList = [
    {
        name: 'Vladislav',
        surname: 'Kudrin',
        middlename: 'Alekseevich',
        faculty: 'IRIT-RTF',
        birthdate: new Date('09-03-2004'),
        startDate: 2022,
    },
    {
        name: 'Serega',
        surname: 'Pirat',
        middlename: 'Bikovich',
        faculty: 'DOTA2',
        birthdate: new Date('2-06-1998'),
        startDate: 2016,
    },
    {
        name: 'Vitaliy',
        surname: 'Tsal',
        middlename: 'Olegovich',
        faculty: 'SAMOKONTROL',
        birthdate: new Date('11-13-1992'),
        startDate: 2000,
    },
    {
        name: 'Gay',
        surname: 'Fox',
        middlename: '',
        faculty: 'UGI',
        birthdate: new Date('10-04-2005'),
        startDate: 2023,
    },
]

// Этап 3. Создайте функцию вывода одного студента в таблицу, по аналогии с тем, как вы делали вывод одного дела в модуле 8. Функция должна вернуть html элемент с информацией и пользователе.У функции должен быть один аргумент - объект студента.

function getStudentItem(studentObj) {
    const table=document.querySelector('.students');
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

    console.log(studentObj.birthdate);
    const birthdate=document.createElement('td');
    const age = `${studentObj.birthdate.toISOString().split('T')[0]} (${(new Date().getFullYear()-studentObj.birthdate.getFullYear())})`;
    switch (age % 10) {
        case 1:
            birthdate.textContent = age + ' год';
            break;
        case 2 || 3 || 4:
            birthdate.textContent = age + ' года';
            break;
        default:
            birthdate.textContent = age + ' лет';
    }

    row.append(birthdate);

    const span=document.createElement('td');
    const difference=new Date().getFullYear()-studentObj.startDate
    span.textContent=`${studentObj.startDate}-${studentObj.startDate+4} (${difference>4?'Закончил':difference+1+' курс'})`;
    row.append(span);

    row.classList.add('student-row');
    return row;
}

// Этап 4. Создайте функцию отрисовки всех студентов. Аргументом функции будет массив студентов.Функция должна использовать ранее созданную функцию создания одной записи для студента.Цикл поможет вам создать список студентов.Каждый раз при изменении списка студента вы будете вызывать эту функцию для отрисовки таблицы.

function renderStudentsTable() {
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
studentForm.addEventListener('submit', (e) => {
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
        birthdate: studentForm.birthday.valueAsDate,
        faculty: studentForm.faculty.value.trim(),
        startDate: Number(studentForm.start.value),
    }

    studentsList.push(student);
    renderStudentsTable();
});

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