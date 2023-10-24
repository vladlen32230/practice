from functools import wraps
import time
from typing import Any

# task_1

def how_are_you(f):
    def wrapper(*args, **kwargs):
        input('Как дела? ')
        print('А у меня не очень!')
        f(*args, **kwargs)
    
    return wrapper

# task_2

def wait(f):
    def wrapper(*args, **kwargs):
        time.sleep(2)
        f(*args, **kwargs)

    return wrapper

# task_3

def log(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print(f.__name__)
        print(f.__doc__)
        try:
            f(*args, **kwargs)
        except Exception as e:
            with open ('function_errors.log', 'w+') as logs:
                logs.write(f'{f.__name__} {e}\n')

    return wrapper

# task_4

class Counter:
    def __init__(self, func) -> None:
        self.f = func
        self.counter = 0

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.counter += 1
        print(f'Количество вызовов функции {self.f.__name__} равно {self.counter}')
        return self.f(*args, **kwargs)
    
# task_5

class Cache:
    def __init__(self, f) -> None:
        self.f = f
        self.cache = dict()

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        if args in self.cache:
            return self.cache[args]
        res = self.f(*args, **kwargs)
        self.cache[args] = res
        return res

@Cache
def fibbo(count):
    num_1 = 1
    num_2 = 0
    cur = 1
    res = []

    while cur <= count:
        res.append(num_1 + num_2)
        num_1, num_2 = num_2, num_1 + num_2
        cur += 1

    return res