from random import randint
from typing import Iterable

# task_1

students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

def get_interests(students: dict[int:dict]) -> list[str]:
    interests = set()

    for student in students.values():
        for interest in student['interests']:
            if interest not in interests:
                interests.add(interest)
    
    return list(interests)

def get_id_age(students: dict[int:dict]) -> list[tuple[int, int]]:
    pairs = []

    for id, student in students.items():
        pairs.append((id, student['age']))

    return pairs

def get_snames_len(students: dict[int:dict]) -> int:
    length = 0

    for student in students.values():
        length += len(student['surname'])

    return length

print(f'Список пар «ID студента — возраст»: {get_id_age(students)}')

print(f'Полный список интересов всех студентов: {get_interests(students)}')

print(f'Общая длина всех фамилий студентов: {get_snames_len(students)}')

# task_2

def is_prime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
        return True
    return False

def crypto(iterable: Iterable):
    return [value for index, value in enumerate(iterable) if is_prime(index)]

# task_3

players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

print([name + scores for name, scores in players.items()])

# task_4

original = [randint(1, 24) for _ in range(10)]

print([tuple((original[i], original[i + 1])) for i in range(0, len(original), 2)])

# task_5

tpl = (6, 3, -1, 8, 4, 10, -5)

for num in tpl:
    if not isinstance(num, int):
        print(tpl)
        break
else:
    print(tuple(sorted(tpl)))

# task_6

contacts = dict()

while True:
    print('1. Добавить контакт')
    print('2. Найти человека')
    action = int(input('Введите номер действия: '))

    if action == 1:
        name, surname = input('Введите имя и фамилию нового контакта (через пробел): ').split(' ')

        if (name, surname) in contacts:
            print('Такой человек уже есть в контактах')
        else:
            number = int(input('Введите номер телефона: '))
            contacts[(name, surname)] = number

    elif action == 2:
        name, surname = input('Введите имя и фамилию нового контакта (через пробел): ').split(' ')

        if (name, surname) in contacts:
            print(f'{name} {surname} {contacts[(name, surname)]}')
        else:
            print('Такого человека нет в контактах')

    else:
        break

    print(f'Текущий словарь контактов: {contacts}')

# task_7

text = 'abcd'
numbers = (10, 20, 30, 40)

generator = ((text[i], numbers[i]) for i in range(min(len(text), len(numbers))))