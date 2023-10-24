# task_1

count = 0

for i in range(10):
    word = input('Крикните слово ')
    if word.lower() == 'карамба':
        count += 1

print(f'{count} достойны быть пиратами!')

# task_2

text = input('Введите текст: ')
print(f'* на {text.find("*")} месте')

# task_3

rows = int(input('Введите количество рядов: '))
seats = int(input('Введите количество сидений в ряде: '))
gap = int(input('Введите количество метров между рядами: '))

print('\nСцена')

for row in range(rows):
    for seat in range(seats):
        print('=', end='')
    print(' ', end='')
    for meter in range(gap):
        print('*', end='')
    print('', end='')
    for seat in range(seats):
        print('=', end='')
    print()

# task_4

x = 8
y = 10

while True:
    direction = input('[Оператор]: ').lower()
    
    if direction == 'w' and y < 20:
        y += 1
    elif direction == 'a' and x > 0:
        x -= 1
    elif direction == 's' and y > 0:
        y -= 1
    elif direction == 'd' and x < 15:
        x += 1
    else:
        break
    
    print(f'[Программа]: Марсоход находится на позиции {x}, {y}, введите команду:')

# task_5

text = input('Введите текст: ')

words = text.split(' ')
max_len = 0

for word in words:
    max_len = max(max_len, len(word))

print(f'Самое длинное слово, букв: {max_len}')

# task_6

free_and_occupied = input('Введите последовательность из f и o: ').split(' ')
res = 0

for place, occupation in enumerate(free_and_occupied):
    if occupation == 'f':
        res += (place + 1) * 2

print(f'Молока за день: {res}')

# task_7

word = input('Введите зашифрованное слово: ')
res = ''

for letter in range(0, len(word), 2):
    res += word[letter]
for letter in range(len(word)-1, 0, -2):
    res += word[letter]

print(f'Слово: {res}')

# task_8

word = input('Введите слово: ')

if word[::-1] == word:
    print('Это палиндром')
else:
    print('Это не палиндром')