import random

# task_1

with open ('people.txt', 'r') as f:
    cur_row = 1
    sum_len = 0

    for row in f.readlines():
        length_str = len(row.replace('\n', ''))
        if length_str < 3:
            print(f'Ошибка: менее трёх символов в строке {cur_row}')
        sum_len += length_str
        cur_row += 1

    print(f'Общее количество символов: {sum_len}')

# task_2

with open('out_file.txt', 'w+') as f:
    nums_sum = 0
    while nums_sum < 777:
        num = int(input('Введите число: '))

        if random.randint(1, 13) == 13:
            raise Exception('Вас постигла неудача')
        
        nums_sum += num
        f.write(f'{num}\n')
    
    print('Вы успешно выполнили условие для выхода из порочного цикла!')

# task_3

with open('registrations.txt', 'r') as reg, open('registrations_good.log', 'w+') as reg_good, open('registrations_bad.log', 'w+') as reg_bad:
    for row in reg.readlines():
        credentials = row.replace('\n', '').split(' ')

        if len(credentials) != 3:
            reg_bad.write(f'{" ".join(credentials)}\tДолжны быть только 3 поля\n')
        else:
            name, email, age = credentials
            if len(name) != len([letter for letter in name if letter.isalpha()]):
                reg_bad.write(f'{name} {email} {age}\tВ имени должны быть только буквы\n')
            elif not '@' in email or not '.' in email:
                reg_bad.write(f'{name} {email} {age}\tПоле «Имейл» НЕ содержит @ или точку\n')
            elif int(age) < 10 or int(age) > 99:
                reg_bad.write(f'{name} {email} {age}\t Поле «Возраст» НЕ представляет число от 10 до 99\n')
            else:
                reg_good.write(f'{name} {email} {age}\n')

# task_4

with open('chat.txt', 'r+') as f:
    while True:
        print('1) Посмотреть текущий текст чата\n2) Отправить сообщение')
        action = int(input('Введите номер действия: '))
        if action == 1:
            f.seek(0)
            for row in f.readlines():
                print(row.rstrip('\n'))
        elif action == 2:
            name = input('Введите имя пользователя: ')
            message = input('Введите сообщение: ')
            f.write(f'{name}: {message}\n')
        else:
            break

# task_5

def take_sqrt(num):
    try:
        num = int(num)
        if num < 0:
            raise ValueError('Число меньше 0')
        return num ** 0.5
    except Exception as exc:
        print(exc)