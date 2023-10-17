# task_1

exp = int(input('Введите количество опыта: '))

if exp < 1000:
    print('Ваш уровень: 1')
elif exp < 2500:
    print('Ваш уровень: 2')
elif exp < 5000:
    print('Ваш уровень: 3')
else:
    print('Ваш уровень: 4')

# task_2

x = int(input('Введите икс: '))

if x > 0:
    y = x - 12
    print(f'игрек равен {y}')
elif x == 0:
    y = 5
    print(f'игрек равен {y}')
else:
    y = x ** 2
    print(f'игрек равен {y}')

# task_3

place = int(input('Введите место в списке поступающих: '))
score = int(input('Введите количество баллов за экзамены: '))

if place > 10:
    print('К сожалению, вы не поступили.')
else:
    print('Поздравляем, вы поступили!')
    if score < 290:
        print('Но вам не хватило баллов для стипендии.')
    else:
        print('Бонусом вам будет начисляться стипендия.')

# task_4

rating = int(input('Что получил по математике? '))

if rating == 2 or rating == 3:
    print('Плохо. Марш учиться!')
elif rating == 4 or rating == 5:
    print('Молодец! Можешь отдохнуть.')

# task_5

num_1 = int(input('Введите 1 число: '))
num_2 = int(input('Введите 2 число: '))
num_3 = int(input('Введите 3 число: '))

if num_1 == num_2 and num_1 == num_3:
    print(3)
elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
    print(2)
else:
    print(0)

# task_6

price = int(input('Введите цену: '))
square = int(input('Введите площадь: '))

if price < 10_000_000 and square >= 100 or price < 7_000_000 and square >= 80:
    print('Квартира подходит')
else:
    print('Квартира не подходит')

# task_7

hours = int(input('Введите время дня в часах: '))

if hours >= 8 and hours < 10 or hours >= 12 and hours < 14 or hours >= 15 and hours < 18 or hours >= 20 and hours < 22:
    print('Можно получить посылку')
else:
    print('Посылку получить нельзя')