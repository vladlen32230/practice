# task_1

n = int(input('Введите последнее число: '))
cur = 1

while cur <= n:
    print(cur ** 3)
    cur += 1

# task_2

name = input('Ваше имя: ')
debt = int(input('Ваш долг: '))

payment = int(input('Введите оплату: '))
while payment < debt:
    print(f'Маловато, {name}. Давайте ещё раз.')
    payment = int(input('Введите оплату: '))
print(f'Отлично, {name}! Вы погасили долг. Спасибо!')

# task_3

num = int(input('Введите число: '))
digits = 1
while num >= 10:
    num //= 10
    digits += 1
print(f'Количество цифр в числе: {digits}')

# task_4

num = int(input('Введите число от -100 до 100: '))
positive = 0
negative = 0
while num != 0:
    if num > 0:
        positive += 1
    else:
        negative += 1
    num = int(input('Введите число от -100 до 100: '))

print(f'Кол-во положительных чисел: {positive}')
print(f'Кол-во отрицательных чисел: {negative}')

# task_5

print('Начался восьмичасовой рабочий день.')

tasks = 1
groceries = False
hour = 1

while hour <= 8:
    completed_tasks = int(input('Сколько задач решит Максим? '))
    tasks += completed_tasks

    wife_call = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет): '))
    if wife_call == 1:
        groceries = True
    hour += 1

print(f'Рабочий день закончился. Всего выполнено задач: {tasks}')

if groceries:
    print('Нужно зайти в магазин.')

# task_6

deposit = int(input('Введите сумму вклада: '))
goal = int(input('Введите желаемую сумму: '))
percent = int(input('Введите годовой процент вклада (без знака "%"): '))

years = 0
while deposit < goal:
    deposit += int(deposit * percent * 0.01)
    years += 1

print(f'Вы накопите желаемую сумму через {years} лет')

# task_7

answer = 7
guess = int(input('Введите число: '))
attempts = 1
while guess != answer:
    if guess > answer:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
    else:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
    attempts += 1
    guess = int(input('Введите число: '))

print(f'Вы угадали! Число попыток: {attempts}')

# task_8

n = int(input('Введите число: '))

left = 1
right = 100
while True:
    cur = (left + right) // 2
    diff = int(input(f'Твоё число равно, меньше или больше, чем число {cur}? (1-равно, 2-больше, 3-меньше)'))
    if diff == 2:
        left = cur + 1
    elif diff == 3:
        right = cur - 1
    else:
        print(f'Твоё число: {cur}')
        break