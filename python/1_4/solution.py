# task_1

raining = int(input('Идёт ли сейчас дождь? '))

if raining:
    print('Пошёл дождь. Возьмите зонтик!')
else:
    print('Дождя нет!')

# task_2

russian = int(input('Введите количество баллов по русскому языку: '))
math = int(input('Введите количество баллов по математике: '))
comp_science = int(input('Введите количество баллов по информатике: '))

if russian + math + comp_science >= 270:
    print('Поздравляю, ты поступил на бюджет!')
else:
    print('К сожалению, ты не прошёл на бюджет.')

# task_3

num = int(input('Введите целое число: '))

if num % 2 == 0:
    print('Число чётное')
else:
    print('Число нечётное')

# task_4

first_good = int(input('Цена первого товара: '))
second_good = int(input('Цена второго товара: '))
third_good = int(input('Цена третьего товара: '))

price = first_good + second_good + third_good
if price >= 10000:
    price = price - price // 10
    print(f'Цена с учётом скидки: {price}')
else:
    print(f'Цена без учёта скидки: {price}')

# task_5

num = int('Введите число: ')

if num < 0:
    print(f'Абсолютная величина: {num}')
else:
    print(f'Абсолютная величина: {-num}')

# task_6

player_score = int(input('Кубик игрока: '))
owner_score = int(input('Кубик владельца: '))

if player_score > owner_score:
    print('Владелец платит')
elif player_score < owner_score:
    print('Игрок платит')
else:
    print('Ничья')
print('Игра окончена!')

# task_7

hours = int(input('Введите отработанные часы: '))
debt = int(input('Введите остаток по кредиту: '))
food = int(input('Введите траты на еду: '))

paycheque = 200 * hours / 2 ** 3 + hours

if paycheque >= debt + food:
    print('Часов хватает. Можно отдохнуть')
else:
    print('Часов не хватает. Придётся работать больше!')

# task_8

num_1 = int(input('Введите 1-ое число: '))
num_2 = int(input('Введите 2-ое число: '))
num_3 = int(input('Введите 3-ое число: '))

if num_1 >= num_2 and num_1 >= num_3:
    print(f'Самое большое число: {num_1}')
if num_2 >= num_1 and num_2 >= num_3:
    print(f'Самое большое число: {num_2}')
else:
    print(f'Самое большое число: {num_3}')