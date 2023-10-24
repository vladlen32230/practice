from functools import reduce

# task_1

floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers = [22, 33, 10, 6894, 11, 2, 1]

floats_new = map(lambda num: round(num ** 3, 3), floats)
names_new = filter(lambda name: len(name) >= 5, names)
numbers_new = reduce(lambda prev, num: num * prev, numbers, 1 if len(numbers) != 0 else 0)

# task_2

letters = ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

results = map(lambda letter, number: (letter, number), letters, numbers)

# task_3

can_be_poly = lambda string: string == string[::-1]

# task_4

count_unique_characters = lambda string: len(list(filter(lambda letter: (string.count(letter.lower()) + string.count(letter.upper())) == 1 and letter != ' ', string)))