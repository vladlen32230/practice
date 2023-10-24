# task_1

violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

count = int(input('Сколько песен выбрать? '))

time = 0

for i in range(count):
    song = input(f'Название {i + 1} песни: ')
    if song in violator_songs:
        time += violator_songs[song]

print(f'Общее время звучания песен: {time} минуты')

# task_2

data = {
    "address": "0x544444444444",
    "ETH": {
    "balance": 444,
    "totalIn": 444,
    "totalOut": 4
    },

    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
            "address": "0x44444",
            "name": "fdf",
            "decimals": 0,
            "symbol": "dsfdsf",
            "total_supply": "3228562189",
            "owner": "0x44444",
            "last_updated": 1519022607901,
            "issuances_count": 0,
            "holders_count": 137528,
            "price": False
            },

            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },

        {
            "sec_token_info": {
            "address": "0x44444",
            "name": "ggg",
            "decimals": "2",
            "symbol": "fff",
            "total_supply": "250000000000",
            "owner": "0x44444",
            "last_updated": 1520452201,
            "issuances_count": 0,
            "holders_count": 20707,
            "price": False
            },

            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

print(data.keys())
print(data.values())

data['ETH']['total_diff'] = 100

data['tokens'][0]['fst_token_info']['name'] = 'doge'

data['ETH']['totalOut'] += data['tokens'][0]['total_out']
del data['tokens'][0]['total_out']
data['ETH']['totalOut'] += data['tokens'][1]['total_out']
del data['tokens'][1]['total_out']

data['tokens'][1]['sec_token_info']['total_price'] = data['tokens'][1]['sec_token_info'].pop('price')

# task_3

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],

    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],

    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],

    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for good, good_id in goods.items():
    sum_price = 0
    sum_quantity = 0

    for sell in store[good_id]:
        sum_price += sell['quantity'] * sell['price']
        sum_quantity += sell['quantity']
    
    print(f'{good} — {sum_quantity} штук, стоимость {sum_price} рублей.')

# task_4

text = input('Введите текст: ')

freq = dict()

for letter in text:
    if letter in freq:
        freq[letter] += 1
    else:
        freq[letter] = 1

inv_freq = dict()

for letter, count in freq.items():
    if count in inv_freq:
        inv_freq[count].append(letter)
    else:
        inv_freq[count] = [letter]

print(f'Оригинальный словарь частот:\n{freq}')
print(f'Инвертированный словарь частот:\n{inv_freq}')

# task_5

count = int(input('Введите количество пар слов: '))

pairs_1 = dict()
pairs_2 = dict()

for i in range(count):
    pairs = input(f'{i + 1} пара: ').split['-']
    word_1, word_2 = pairs[0].strip().lower(), pairs[1].strip().lower()
    pairs_1[word_1] = word_2
    pairs_2[word_2] = word_1

while True:
    word = input('Введите слово: ')
    if word in pairs_1:
        print(f'Синоним: {pairs_1[word]}')
        break
    elif word in pairs_2:
        print(f'Синоним: {pairs_2[word]}')
        break
    else:
        print('Такого слова в словаре нет')

# task_6

count = int(input('Введите количество заказов: '))

orders = dict()

for i in range(count):
    order = input(f'{i + 1} заказ: ').split(' ')
    name, pizza, quantity = order
    
    if name in orders:
        if pizza in orders[name]:
            orders[name][pizza] += quantity
        else:
            orders[name][pizza] = quantity
    else:
        orders[name] = dict()
        orders[name][pizza] = quantity

for name, order in orders.items():
    print(f'{name}: \n{order}')

# task_7

array_1 = [1, 5, 10, 20, 40, 80, 100]

array_2 = [6, 7, 20, 80, 100]

array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

res = []

for num in array_1:
    if num in array_2 and num in array_3:
        res.append(num)

print(f'Решение без множеств задачи 1: {res}')

res.clear()

for num in array_1:
    if num not in array_2 and num not in array_3:
        res.append(num)

print(f'Решение без множеств задачи 2: {res}')

set_1, set_2, set_3 = set(array_1), set(array_2), set(array_3)

print(f'Решение с множествами задачи 1: {set_1.intersection(set_2).intersection(set_3)}')

print(f'Решение с множествами задачи 2: {set_1.difference(set_2).difference(set_3)}')

# task_8

text = input('Введите строку: ')

for shift in range(len(text)):
    if text[shift::] + text[0:shift:] == text[::-1]:
        print(f'Можно сделать палиндромом')
        break
else:
    print('Нельзя сделать палиндромом')