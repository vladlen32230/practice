# task_1

text = input('Введите текст: ')

letters = [letter for letter in text if letter in set("аоуыэяюёиеАОУЫЭЯЮЁИЕ")]

print(f'Список гласных букв: {letters}')
print(f'Длина списка: {len(letters)}')

# task_2

length = int(input('Введите длину списка: '))

res = [1 if i % 2 == 0 else i % 5 for i in range(length)]
print(f'Результат: {res}')

# task_3

first_team = [7.86, 6.76, 9.97, 9.08, 5.45, 6.9, 8.65, 5.17, 8.17, 5.06, 7.56, 7.1, 7.18, 8.25, 5.53, 7.95, 8.91, 7.11, 8.29, 9.52]
second_team = [7.13, 5.7, 8.89, 5.36, 5.62, 9.46, 5.82, 8.67, 8.41, 7.0, 5.31, 7.8, 9.93, 7.76, 7.4, 8.26, 7.94, 5.71, 7.89, 7.77]

winner = [first_team[i] if first_team[i] > second_team[i] else second_team[i] for i in range(len(first_team))]
print(winner)

# task_4

alphabet = 'abcdefg'

print(alphabet[::])
print(alphabet[::-1])
print(alphabet[::2])
print(alphabet[1::2])
print(alphabet[:1:])
print(alphabet[len(alphabet) - 1:len(alphabet) - 2:-1])
print(alphabet[3:4:])
print(alphabet[len(alphabet) - 3::])
print(alphabet[3:5:])
print(alphabet[4:2:-1])

# task_5

text = input('Введите строку: ')

left = text.find('h')
right = text.rfind('h')

print(f'Развёрнутая последовательность между первым и последним h: {text[left + 1:right:1]}')

# task_6

res = [[i + 1, i + 5, i + 9] for i in range(4)]
print(res)

# task_7

nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

print([i for j in nice_list for k in j for i in k])

# task_8

message = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
alphabet = 'абвгдёежзийклмнопрстуфхцчшщьыъэюя'

def encrypt(letter):
    index = alphabet.find(letter)
    return alphabet[(index + shift) % len(alphabet)]

print(f'Зашифрованное сообщение: {"".join([encrypt(letter) if letter in alphabet else letter for letter in message])}')