function createTodoApp(title, ownership) {
    function createTodoItemForm() {
        const form=document.createElement('form');
        const input=document.createElement('input');
        const buttonWrapper=document.createElement('div');
        const button=document.createElement('button');
        const titleHead=document.createElement('h2');

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

        localStorage.getItem(ownership) == null && localStorage.setItem(ownership, JSON.stringify({}));

        return {
            titleHead,
            form,
            input,
            button,
        };
    }
    

    function createTodoList() {
        const list=document.createElement('ul');
        list.classList.add('list-group');
        return list;
    }

    const container=document.querySelector('#todo-app');

    const todoItemForm=createTodoItemForm();
    const todoList=createTodoList();

    todoItemForm.input.addEventListener('input', () => todoItemForm.button.disabled = todoItemForm.input.value.length === 0);

    container.append(todoItemForm.titleHead);
    container.append(todoItemForm.form);
    container.append(todoList);

    function createTodoItem(name, done=false, id=null) {
        if (id===null) {
            id=Math.random().toString(16).slice(2);
        }

        const item=document.createElement('li');
        const buttonGroup=document.createElement('div');
        const doneButton=document.createElement('button');
        const deleteButton=document.createElement('button');

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
            const todos = JSON.parse(localStorage.getItem(ownership));
            todos[id].done = !todos[id].done;
            localStorage.setItem(ownership, JSON.stringify(todos));
        });

        deleteButton.addEventListener('click', function() {
            if (confirm('Вы уверены?')) {
                item.remove(); 
                const todos = JSON.parse(localStorage.getItem(ownership));
                delete todos[id];
                localStorage.setItem(ownership, JSON.stringify(todos));
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

        const todoItem=createTodoItem(todoItemForm.input.value, false, null);
        const todos = JSON.parse(localStorage.getItem(ownership));
        todos[todoItem.id] = {
            name: todoItem.name,
            done: false
        };

        localStorage.setItem(ownership, JSON.stringify(todos));

        todoList.append(todoItem.item);

        todoItemForm.input.value='';
    });

    (function fetchData() {
        const todos = JSON.parse(localStorage.getItem(ownership));
        for (const [id, data] of Object.entries(todos)) {
            const todoItem = createTodoItem(data.name, data.done, id);
            todoList.append(todoItem.item);
        }
    })();
};