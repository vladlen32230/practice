import random
from abc import ABC, abstractmethod

# task_1

class Property:
    def __init__(self, worth) -> None:
        self.worth = worth

class Apartment(Property):
    def __init__(self, worth) -> None:
        super().__init__(worth)
    
    def count_taxes(self):
        return self.worth / 1000

class Car(Property):
    def __init__(self, worth) -> None:
        super().__init__(worth)

    def count_taxes(self):
        return self.worth / 200

class CountryHouse(Property):
    def __init__(self, worth) -> None:
        super().__init__(worth)

    def count_taxes(self):
        return self.worth / 500
    
# task_2

class KillError(Exception):
    def __init__(self, message='You killed somebody'):
        self.message = message
        super().__init__(message)

class GluttonyError(Exception):
    def __init__(self, message='You are overeating'): 
        self.message = message
        super().__init__(message)

class CarCrashError(Exception):
    def __init__(self, message='You have committed car crash'):
        self.message = message
        super().__init__(message)

def one_day():
    if random.randint(1, 30) == 10:
        raise KillError
    elif random.randint(1, 30) == 10:
        raise GluttonyError
    elif random.randint(1, 30) == 10:
        raise CarCrashError
    else:
        return random.randint(1, 7)
    
karma_max = 500
cur_karma = 0

with open('karma.log', 'w') as f:
    while cur_karma < karma_max:
        try:
            cur_karma += one_day()
        except Exception as e:
            f.write(f'{e.message}\n')

# task_3

class MyDict(dict):
    def __init__(self) -> None:
        super().__init__(self)
        
    def get(self, item):
        if item in self:
            return self[item]
        return 0

# task_4

# no material

# task_5

class Stack(list):
    def __init__(self):
        super().__init__(self)

class TaskManager:
    def __init__(self) -> None:
        self.tasks = dict()

    def new_task(self, task, priority):
        if priority in self.tasks:
            self.tasks[priority].append(task)
        else:
            self.tasks[priority] = [task]
    
    def __str__(self) -> str:
        keys = sorted(self.tasks.keys())
        return '\n'.join([f'{key} - {"; ".join(self.tasks[key])}' for key in keys])
    
# task_6

class Shape(ABC):
    @abstractmethod
    def area():
        pass

class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        return 3.141596 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width
    
class Triangle(Shape):
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        half_p = (self.a + self.b + self.c) / 2
        return (half_p * (half_p - self.a) * (half_p - self.b) * (half_p - self.c)) ** 0.5