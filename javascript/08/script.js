function createTodoApp(title, ownership) {
    function createTodoItemForm() {
        let form=document.createElement('form');
        let input=document.createElement('input');
        let buttonWrapper=document.createElement('div');
        let button=document.createElement('button');
        let titleHead=document.createElement('h2');

        titleHead.textContent=title;
        form.classList.add('input-group', 'mb-3');
        input.classList.add('form-control');
        input.placeholder='Введите название нового дела';
        buttonWrapper.classList.add('input-group-append');
        button.classList.add('btn', 'btn-primary');
        button.textContent='Добавить дело';
        button.disabled=true;

        buttonWrapper.append(button);
        form.append(input);
        form.append(buttonWrapper);

        return {
            titleHead,
            form,
            input,
            button,
        };
    }
    

    function createTodoList() {
        let list=document.createElement('ul');
        list.classList.add('list-group');
        return list;
    }

    let container=document.querySelector('#todo-app');

    let todoItemForm=createTodoItemForm();
    let todoList=createTodoList();

    todoItemForm.input.addEventListener('input', function() {
        if (todoItemForm.input.value.length===0) {
            todoItemForm.button.disabled=true;
        } else {
            todoItemForm.button.disabled=false;
        }
    });

    container.append(todoItemForm.titleHead);
    container.append(todoItemForm.form);
    container.append(todoList);

    function createTodoItem(name, done=false, id=null) {
        if (id===null) {
            id='todoapp-'+Math.random().toString(16).slice(2);
        }

        let item=document.createElement('li');
        let buttonGroup=document.createElement('div');
        let doneButton=document.createElement('button');
        let deleteButton=document.createElement('button');

        item.classList.add('list-group-item', 'd-flex', 'justify-content-between', 'align-items-center');
        item.textContent=name;

        buttonGroup.classList.add('btn-group', 'btn-group-sm');
        doneButton.classList.add('btn', 'btn-success');
        doneButton.textContent='Готово';
        deleteButton.classList.add('btn', 'btn-danger');
        deleteButton.textContent='Удалить';

        if (done) {
            item.classList.add('list-group-item-success');
        }

        buttonGroup.append(doneButton);
        buttonGroup.append(deleteButton);
        item.append(buttonGroup);

        doneButton.addEventListener('click', function() {
            item.classList.toggle('list-group-item-success');
            let obj=JSON.parse(localStorage.getItem(id));
            obj.done=!obj.done;
            localStorage.setItem(id, JSON.stringify(obj));
        });

        deleteButton.addEventListener('click', function() {
            if (confirm('Вы уверены?')) {
                item.remove(); 
                localStorage.removeItem(id);
            }
        });

        return {
            id,
            item,
            name,
        };
    }

    todoItemForm.form.addEventListener('submit', function(e) {
        e.preventDefault();
        if (!todoItemForm.input.value) {
            return;
        }

        let todoItem=createTodoItem(todoItemForm.input.value, false, null);
        localStorage.setItem(todoItem.id, JSON.stringify({
            name: todoItem.name,
            done: false,
            ownership,
        }));

        todoList.append(todoItem.item);

        todoItemForm.input.value='';
    });

    (function fetchData() {
        for (let [id, data] of Object.entries(localStorage)) {
            data=JSON.parse(data);
            if (id.startsWith('todoapp-') && data.ownership===ownership) {
                todoItem=createTodoItem(data.name, data.done, id);
                todoList.append(todoItem.item);
            }
        }
    })();
};