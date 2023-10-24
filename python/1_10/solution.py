# task_1

for row in range(6):
    for col in range(6):
        print(row + col * 2, end='\t')
    print()

# task_2

rows = int(input('Введите число: '))
for row in range(1, rows + 1):
    for col in range(row):
        print(row, end=' ')
    print()

# task_3

height = int(input('Введите высоту: '))
width = int(input('Введите ширину: '))

for row in range(height):
    for col in range(width):
        if col == 0 or col == width - 1:
            print('|', end='')
        elif row == 0 or row == height - 1:
            print('-', end='')
        else:
            print(' ', end='')
    print()

# task_4

count = int(input('Введите количество чисел: '))
res = 0

for _ in range(count):
    number = int(input('Введите число: '))
    for div in range(2, number // 2 + 1):
        if number % div == 0:
            break
    else:
        res += 1

print(f'Количество простых чисел в последовательности: {res}')

# task_5

count = int(input('Введите количество чисел: '))
res_num = 0
res_digits_sum = 0

for _ in range(count):
    number = int(input('Введите число: '))
    num = number
    digits_sum = 0

    while True:
        digits_sum += num % 10
        num //= 10
        if num == 0:
            break
    
    if digits_sum > res_digits_sum:
        res_digits_sum = digits_sum
        res_num = number

print(f'Число {res_num} имеет самую большую сумму цифр, равной {res_digits_sum}')

# task_6

height = int(input('Введите высоту: '))

width = (height - 1) * 2 + 1

for row in range(height):
    print(' ' * (height - row - 1), end='')
    print('#' * (row * 2 + 1), end='')
    print(' ' * (height - row - 1))

# task_7

height = int(input('Введите высоту: '))
number = 1

for row in range(height):
    print('   ' * (height - row - 1), end='')

    for col in range(row + 1):
        print(number, end='')
        number += 2
        if number != row:
            print('   ', end='')
    print('   ' * (height - 1))

# task_8

depth = int(input('Введите глубину: '))
width = depth * 2

for row in range(1, depth + 1):
    for col in range(row):
        print(depth - col, end='')
    print('.' * ((depth - row) * 2), end='')
    for col in range(row):
        print(depth - (row - col - 1), end='')
    print()