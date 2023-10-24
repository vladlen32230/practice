# task_1

pos_and_even = 0

for i in range(1, 11):
    num = int(input(f'Введите {i}-ое число: '))
    if num > 0 and num % 2 == 0:
        pos_and_even += 1

print(f'Количество чётных и положительных чисел: {pos_and_even}')

# task_2

sum = 0

for month in range(1, 13):
    paycheque = int(input(f'Введите зарплату за {month} месяц: '))
    sum += paycheque

print(f'Средняя зарплата за год: {sum // 12}')

# task_3

n = int(input('Введите число: '))
fact = n
res = 1

while n != 1:
    res *= n
    n -= 1

print(f'Факториал числа {fact} равен {res}')

# task_4


three, four, five = 0, 0, 0
students = int(input('Введите количество студентов: '))

for student in range(1, students + 1):
    grade = int(input(f'Какую оценку получил {student} студент: '))
    if grade == 3:
        three += 1
    elif grade == 4:
        four += 1
    elif grade == 5:
        five += 1

if three > four and three > five:
    print('Больше всего троечников')
elif four > three and four > five:
    print('Больше всего хорошистов')
else:
    print('Больше всего отличников!')

# task_5

num_1 = int(input('Введите 1 число: '))
num_2 = int(input('Введите 2 число: '))

count = 0
sum = 0

for num in range(num_1, num_2 + 1):
    if num % 3 == 0:
        count += 1
        sum += num

print(f'Среднее арифметическое кратных трём равно: {sum / count}')

# task_6

for num in range(10, 100):
    digit_1 = num % 10
    digit_2 = num // 10
    if digit_1 * digit_2 * 3 == num:
        print(f'{num} является замечательным числом')

# task_7

count = int(input('Введите число карточек: '))
all_cards = set((card for card in range(1, count + 1)))

for card in range(1, count):
    number_card = int(input(f'Введите номер {card} карты'))
    all_cards.remove(number_card)

print(f'Потерянная карта: {all_cards.pop()}')