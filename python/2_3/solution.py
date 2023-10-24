# task_1

main = [1, 5, 3]
auxiliary_1 = [1, 5, 1, 5]
auxiliary_2 = [1, 3, 1, 5, 3, 3]

main.extend(auxiliary_1)

print(main.count(5))

main = list(filter(lambda num: num != 5, main))

main.extend(auxiliary_2)

print(main.count(3))

print(main)

# task_2

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]

def merge_sorted_lists(list_1, list_2):
    first, second = 0, 0
    values = set()
    res = []

    while first < len(list_1) or second < len(list_2):
        if second == len(list_2) or first != len(list_1) and list_1[first] < list_2[second]:
            if list_1[first] not in values:
                res.append(list_1[first])
                values.add(list_1[first])
            first += 1
        else:
            if list_2[second] not in values:
                res.append(list_2[second])
                values.add(list_2[second])
            second += 1
    
    return res

merged = merge_sorted_lists(list1, list2)

print(merged)

# task_3

shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]

name = input('Название детали: ')
count = int(input('Количество деталей: '))

for detail in shop:
    if detail[0] == name:
        print(f'Общая стоимость: {count * detail[1]}')
        break

# task_4

guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f'Сейчас на вечеринке 5 человек: {guests}')
    
    action = input('Гость пришёл или ушёл? ')
    if action == 'пришёл':
        name = input('Имя гостя: ')
        if len(guests) < 6:
            print(f'Привет, {name}!')
            guests.append(name)
        else:
            print(f'Прости, {name}, но мест нет.')
    elif action == 'ушёл':
        name = input('Имя гостя: ')
        guests.remove(name)
        print(f'Пока, {name}!')
    else:
        break

# task_5

violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

count = int(input('Сколько песен выбрать? '))
time = 0

for num in range(count):
    name = input(f'Название {num + 1}-й песни:')
    for song in violator_songs:
        if song[0] == name:
            time += song[1]
            break

print(f'Общее время звучания песен — {time} минуты')

# task_6

count_rollers = int(input('Количество роликов: '))
rollers = []

for roller in range(count_rollers):
    size = int(input(f'Размер пары {roller + 1}: '))
    rollers.append(size)

count_people = int(input('Количество людей: '))
count = 0

for human in range(count_people):
    size = int(input(f'Размер ноги человека {human + 1}: '))
    if size in rollers:
        rollers.remove(size)
        count += 1

print(f'Наибольшее количество людей, которые могут взять ролики: {count}')

# task_7

people_count = int(input('Количество человек: '))
people = [human + 1 for human in range(people_count)]

num = int(input('Какое число в считалке? '))
start = 0
print(f'Значит выбывает каждый {num}-й человек')

while len(people) > 1:
    print(f'Текущий круг людей: {people}')
    print(f'Начало счёта с номера {people[start]}')
    
    shift = num % len(people) - 1
    while shift != 0:
        start += 1
        if start == len(people):
            start = 0
        shift -= 1
    
    print(f'Выбывает человек под номером {people[start]}')
    people.pop(start)
    if start == len(people):
        start = 0
    
print(f'Остался человек под номером {people[0]}')

# task_8

count = int(input('Количество чисел: '))
numbers = []

for _ in range(count):
    number = int(input('Число: '))
    numbers.append(number)

print(f'Последовательность: {numbers}')

start = len(numbers) - 1
div = -1

while start >= 0:
    part = numbers[start:len(numbers)]
    if part[::-1] == part:
        div = start
    start -= 1

extended = numbers[0:div]
extended.reverse()

print(f'Нужно приписать чисел: {len(extended)}')
print(f'Сами числа: {extended}')