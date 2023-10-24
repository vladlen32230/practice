from datetime import datetime
import time
from typing import Any

# task_1

def check_permission(status):
    def outer_wrapper(func):
        def inner_wrapper(*args, **kwargs):
            if status not in user_permissions:
                raise PermissionError
            return func(*args, **kwargs)
        return inner_wrapper

    return outer_wrapper

user_permissions = ['admin']

@check_permission('admin')
def delete_site():
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')

# task_2

def callback(path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            route = dict().get(path)
            if route:
                response = route()
                print('Ответ:', response)
            else:
                print('Такого пути нет')
            return func(*args, **kwargs)
        return wrapper
    return decorator

@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'

# task_3

def log_methods(format: str):
    def decorator(cls):
        def log(func):
            pattern_match = lambda: datetime.now().strftime( (format.replace('b', '%m').replace('d', '%d').replace('Y', '%Y').replace('H', '%H').replace('M', '%M').replace('S', '%S')) )

            def wrapper(*args, **kwargs):
                start = time.time()
                print(f'Запускается {cls.__name__}.{func.__name__}. Дата и время запуска: {pattern_match()}')
                res = func(*args, **kwargs)
                end = time.time()
                print(f'Завершение {cls.__name__}.{func.__name__}, время работы = {round(end - start, 5)} s. ')
                return res
            return wrapper

        for attr_name in dir(cls):
            attr = getattr(cls, attr_name)
            if callable(attr) and not attr_name.startswith('__'):
                setattr(cls, attr_name, log(attr))

        return cls
    return decorator

@log_methods("b d Y — H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")


    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

# task_4

def decorated_decorator(*args_dec, **kwargs_dec):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f'Переданные арги и кварги в декоратор: {args_dec} {kwargs_dec}')
            return func(*args, **kwargs)
        
        return wrapper
    
    return decorator

@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)

# task_5

def singleton(cls):
    def new(self, *args, **kwargs):
        if '_inst' in dir(self):
            return self._inst
        inst = super(cls, self).__new__(self, *args, **kwargs)
        self._inst = inst
        return inst
        
    setattr(cls, '__new__', new)
    return cls

@singleton
class Example:
    pass

# task_6

class LoggerDecorator:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args: Any, **kwargs: Any):
        print(f'Вызов функции {self.func.__name__}')
        print(f'Аргументы: {args}, {kwargs}')

        start_time = time.time()
        res = self.func(*args, **kwargs)
        
        print(f'Результат: {res}')
        print(f'Время выполнения: {time.time() - start_time} секунд')
        return res

@LoggerDecorator
def complex_algorithm(arg1, arg2):
    # Здесь выполняется “сложный” алгоритм
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    # Можете попробовать вынести создание файла из циклов и проверить, сколько времени алгоритм будет работать в этом случае
    return result