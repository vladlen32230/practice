# task_1

menu = input('Введите меню с (;) разделителем: ').split(';')
print(f'Сейчас в меню есть: {", ".join(menu)}')

# task_2

words = input('Введите строку: ').split(' ')

max_word = ''
max_len = 0
for word in words:
    if len(word) > max_len:
        max_word = word
        max_len = len(word)

print(f'Самое длинное слово: {max_word}')
print(f'Длина этого слова: {max_len} символов')

# task_3

name = input('Название файла: ')

prohibited = '@№$%^&*()'

if name.startswith(('@', '№', '$', '%', '^', '&', '*', '(', ')')):
    print('Ошибка: название начинается недопустимым символом.')
elif not name.endswith(('.txt', '.docx')):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
    print('Файл назван верно')

# task_4

text = input('Введите строку: ')
print(f'Результат: {text.title()}')

# task_5

uppercase = set('ABCDEFGHIJKLMOPQRSTUVWXYZ')

while True:
    upper = False
    digits = []
    password = input('Введите пароль: ')

    if len(password) < 8:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
        continue

    for letter in password:
        if letter in uppercase:
            upper = True
        elif letter.isdigit():
            digits.append(letter)
        if upper and len(digits) >= 3:
            print('Это надёжный пароль.')
            break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
        continue
    break

# task_6

text = input('Введите строку: ')

coded = ''

count = 0
prev = ''

for letter in text:
    if letter == prev:
        count += 1
    else:
        if count > 0:
            coded += prev + str(count)
        count = 1
        prev = letter

coded += prev + str(count)

print(f'Закодированная строка: {coded}')

# task_7

ip = input('Введите IP: ').split('.')

if len(ip) != 4:
    print('Адрес — это четыре числа, разделённые точками')
else:
    for num in ip:
        if not num.isnumeric():
            print(f'{num} — это не целое число')
            break
        elif int(num) < 0 or int(num) > 255:
            print(f'{num} должен быть между 0 и 255')
            break
    else:
        print('IP-адрес корректен')

# task_8

str_1 = input('Первая строка: ')
str_2 = input('Вторая строка: ')

if len(str_1) != len(str_2):
    print('Первую строку нельзя получить из второй с помощью циклического сдвига')
else:
    for shift in range(len(str_1)):
        if str_2[shift::] + str_2[0:shift:] == str_1:
            print(f'Первая строка получается из второй со сдвигом {shift}')
            break
    else:
        print('Первую строку нельзя получить из второй с помощью циклического сдвига')

# task_9

def count_uppercase_lowercase(text):
    lower = set('abcdefghijklmnopqrstuvwxyz')
    upper = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    count_lower = 0
    count_upper = 0

    for letter in text:
        if letter in lower:
            count_lower += 1
        elif letter in upper:
            count_upper += 1
    
    return count_upper, count_lower

text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)