# task_1

month = 1

for remain in range(100, -1, -4):
    print(f'В {month} месяце у вас будет {remain} килограмм гречки')
    month += 1

print('Запасы закончились')

# task_2

count = int(input('Введите количество должников: '))
sum_debt = 0

for debtor in range(0, count, 5):
    print(f'Должник с номером {debtor}')
    debt = int(input('Сколько должны? '))
    sum_debt += debt

print(f'Общая сумма долга: {sum_debt}')

# task_3

timer = int(input('Введите количество секунд: '))

for reverse_time in range(timer, 0, -1):
    end = int(input('Закончить? '))
    if end == 1:
        print(f'Ваша еда готова, можете забрать. Оставшееся время было: {reverse_time}')
        break
else:
    print('Ваша еда готова, осторожно горячo!')

# task_4

left = int(input('Введите левую границу: '))
right = int(input('Введите правую границу: '))
divider = int(input('Введите число, на которое должно делиться другое число без остатка: '))

num_sum = 0
num_count = 0

for num in range(left, right + 1):
    if num % divider == 0:
        num_sum += num
        num_count += 1

print(f'Среднее арифметическое: {num_sum / num_count}')

# task_5

start = int(input('Введите начало отрезка: '))
end = int(input('Введите конец отрезка: '))
step = int(input('Введите шаг (отрицательный): '))

for num in range(end, start - 1, step):
    print(f'В точке {num} функция равна {num ** 3 + 2 * num ** 2 - 4 * num + 1}')

# task_6

educational_grant = int(input('Введите стипендию: '))
expenses = int(input('Введите расходы на проживание: '))

for month in range(1, 11):
    print(f'{month} месяц. Траты {expenses}, не хватает {expenses - educational_grant}')

    educational_grant *= 1.03
    expenses *= 1.03

print(f'Нужно попросить у родителей {expenses - educational_grant} рублей')

# task_7

n = int(input('Введите N: '))
res = 0

for i in range(n):
    res += -1 ** i * 1 / 2 ** i

print(res)

# task_8

boys = int(input('Введите количество мальчиков: '))
girls = int(input('Введите количество девочек: '))
people = boys + girls

if boys == 0 and girls == 0:
    print('')
elif boys == 1 and girls == 0:
    print('B')
elif boys == 0 and girls == 1:
    print('G')
elif boys == 1 and girls == 1:
    print('BG')
elif boys / 2 > girls or girls / 2 > boys:
    print('Решения нет')
else:
    res = ''
    last = ''

    if girls > boys:
        res = 'GB'
        last = 'B'
    else:
        res = 'BG'
        last = 'G'
    count = 2
    girls -= 1
    boys -= 1

    while count < people:
        if girls > boys and last != 'GG':
            if res[-1] == 'B':
                last = ''
            res += 'G'
            last += 'G'
            girls -= 1
        elif boys > girls and last != 'BB':
            if res[-1] == 'G':
                last = ''
            res += 'B'
            last += 'B'
            boys -= 1
        else:
            if last == 'GG' or last == 'G':
                res += 'B'
                last = 'B'
                boys -= 1
            else:
                res += 'G'
                last = 'G'
                girls -= 1
        count += 1
    print(res)