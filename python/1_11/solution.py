import math

# task_1

price = float(input('Введите цену в евро: '))

print(f'{price * 1.25 * 60.87} - цена в рублях')

# task_2

count = int(input('Введите кол-во чисел: '))

for _ in range(count):
    num = float(input('Введите число: '))
    if num > 0:
        num = math.ceil(num)
        print(f'log(x) = {math.log(num)}')
    else:
        num = math.floor(num)
        print(f'exp(x) = {math.e ** num}')

# task_3

size = int(input('Укажите размер файла для скачивания: '))
speed = int(input('Какова скорость вашего соединения: '))
time = 1
progress = speed

while progress < size:
    print(f'Прошло {time} секунд. Скачано {progress} из {size} Мб ({int(progress / size * 100)}%)')
    time += 1
    progress += speed

print(f'Прошло {time} секунд. Скачано {size} из {size} Мб (100%)')

# task_4

num = float(input('Введите число: '))

print(f'Первая цифра после точки: {int(num * 10 % 10)}')

# task_5

radius = float(input('Введите радиус планеты: '))

earth_volume = 1.08321e12
planet_volume = 4 / 3 * math.pi * radius ** 3
if planet_volume > earth_volume:
    print(f'Объём планеты Земля больше в {planet_volume / earth_volume} раз')
elif planet_volume < earth_volume:
    print(f'Объём планеты Земля меньше в {earth_volume / planet_volume} раз')
else:
    print('Планеты равны по объему')

# task_6

print('Введите местоположение коня: ')
x_start = int(float(input()) * 10)
y_start = int(float(input()) * 10)

print('Введите местоположение точки на доске: ')
x_end = int(float(input()) * 10)
y_end = int(float(input()) * 10)

print(f'Конь в клетке ({x_start}, {y_start}). Точка в клетке ({x_end}, {y_end})')

if abs(x_end - x_start) == 2 and abs(y_end - y_start) == 1 or abs(x_end - x_start) == 1 and abs(y_end - y_start) == 2:
    print('Да, конь может ходить в эту точку')
else:
    print('Нет, конь не может ходить в эту точку')

# task_7

num_1 = float(input('Введите первое число: '))
num_2 = float(input('Введите второе число: '))

print(f'Наибольшее число: {(abs(num_1 - num_2) + (num_1 + num_2)) / 2}')