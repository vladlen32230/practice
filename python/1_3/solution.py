# task_1

a = 8

b = 10

c = 12

d = 18

res = (( -3 + a ** 2) * b - 2 ** 3) / (c - 2 * d)

print(res)

# task_2

num1 = float(input('Введите 1 число: '))
num2 = float(input('Введите 2 число: '))
num3 = float(input('Введите 3 число: '))
num4 = float(input('Введите 4 число: '))

num1_num2 = num1 + num2
num3_num4 = num3 + num4
res = num1_num2 / num3_num4

print(res)

# task_3

num = int(input('Введите число: '))

next_num = num + 1
prev_num = num - 1

print(f'После числа {num} идёт число {next_num}')
print(f'До числа {num} идёт число {prev_num}')

# task_4

cathet_1 = float(input('Введите длину 1-го катета: '))
cathet_2 = float(input('Введите длину 2-го катета: '))

print(f'Площадь треугольника равна {(cathet_1 * cathet_2) / 2}')

# task_5

minutes = int(input('Введите количество минут: '))

hours = minutes // 60
minutes_remain = minutes % 60

print(f'Кол-во часов: {hours}\nКол-во оставшихся минут: {minutes_remain}')

# task_6

num_1 = int(input('Введите 1-ое 3-ёхзначное число: '))
num_2 = int(input('Введите 2-ое 3-ёхзначное число: '))

last_2digits_1 = num_1 % 100
last_2digits_2 = num_2 % 100

print(f'Сумма: {last_2digits_1 + last_2digits_2}')

# task_7

num = int(input('Введите 4-ёхзначное число: '))

print(f'1-ая цифра числа: {num // 1000}')
print(f'2-ая цифра числа: {num // 100 % 10}')
print(f'3-я цифра числа: {num // 10 % 10}')
print(f'4-ая цифра числа: {num % 10}')

# task_8

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

print(a, b)

a = a + b
b = a - b
a = a - b

print(a, b)