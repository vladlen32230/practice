# task_1

count = int(input('Введите число: '))

res = [num for num in range(1, count + 1, 2)]

print(res)

# task_2

names = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']

even_names = [names[name] for name in range(0, len(names), 2)]

print(f'Первый день: {even_names}')

# task_3

count = int(input('Введите количество: '))

videocards = []
for i in range(count):
    videocard = int(input(f'Видеокарта {i + 1}: '))
    videocards.append(videocard)

latest_videocard = max(videocards)

print(f'Новый список видеокарт: {[videocard for videocard in videocards if videocard != latest_videocard]}')

# task_4

films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']

count = int(input('Сколько фильмов хотите добавить? '))

favourites = []
for _ in range(count):
    film = input('Введите название фильма: ')
    if film in films:
        favourites.append(film)
    else:
        print(f'Ошибка: фильма {film} у нас нет :(')

print(f'Ваш список любимых фильмов: {" ".join(favourites)}')

# task_5

count = int(input('Количество контейнеров: '))

containers = []

prev = float('inf')
for _ in range(count + 1):
    weight = int(input('Введите вес контейнера: '))
    if weight <= prev and weight <= 200:
        containers.append(weight)
        prev = weight
    else:
        print('Введен вес больший 200 или не в порядке убывания')
        break

new_weight = int(input('Введите вес нового контейнера: '))
for number, weight in enumerate(containers):
    if weight >= new_weight:
        print(f'Номер, который получит новый контейнер: {number + 1}')

# task_6

shift = int(input('Сдвиг: '))

list_old = input('Введите изначальный список (через пробел): ').split(' ')
list_new = list_old[shift - 1:len(list_old)] + list_old[0:shift - 1]

print(f'Сдвинутый список: {list_new}')

# task_7

word = input('Введите слово: ')

if word == word[::-1]:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')

# task_8

list_old = [1, 4, -3, 0, 10]

print(f'Отсортированный список: {list_old.sort()}')

# task_9

test = [1, 3, 2, 7, 9, 11, 12, 4, 6, 0, 22, 8, 21]

for i in range(len(test) - 1, -1, -1):
    if test[i] % 2 != 0:
        test.pop(i)

left = 0
right = len(test) - 1

while right > left:
    test[left], test[right] = test[right], test[left]
    right -= 1
    left += 1

print(f'Новый список: {test}')