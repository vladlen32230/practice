from typing import Iterable

# task_1

end = int(input('Введите num: '))

def print_num(cur):
    print(cur)
    if cur != end:
        print_num(cur + 1)

print_num(1)

# task_2

site = {
'html': {
        'head': {
            'title': 'Мой сайт'
        },

        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

key_needed = input('Введите искомый ключ: ')

max_depth = float('inf')
depth_change = input('Хотите ввести максимальную глубину? Y/N: ')
if depth_change == 'y':
    max_depth = int(input('Введите максимальную глубину: '))

res_item = None

def traverse(cur_depth, item):
    if cur_depth == max_depth:
        return
    global res_item
    
    for key in item:
        if res_item:
            return
        
        if key == key_needed:
            res_item = item[key]

        if isinstance(item[key], dict):
            traverse(cur_depth + 1, item[key])

traverse(0, site)
print(res_item)

# task_3

count = int(input('Сколько сайтов: '))

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },

        'body': {
            'h2': 'У нас самая низкая цена на телефон',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

def create_copy(dictionary: dict, new_word):
    return _create_copy(dictionary.copy(), new_word)

def _create_copy(dictionary: dict, new_word):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            dictionary[key] = value.copy()
            _create_copy(dictionary[key], new_word)
        elif isinstance(value, str):
            dictionary[key] = value.replace('телефон', new_word)
    
    return dictionary

for _ in range(count):
    product = input('Введите название продукта для нового сайта: ')
    print(f'Сайт для {product}: {create_copy(site, product)}')

# task_4

def sum(*args):
    res_sum = 0

    def _sum(args):
        for value in args:
            if isinstance(value, Iterable):
                _sum(value)
            elif isinstance(value, (int, float)):
                nonlocal res_sum
                res_sum += value
    
    _sum(args)
    return res_sum
    
print(sum([[1, 2, [3]], [1], 3]))
print(sum(1, 2, 3, 4, 5))

# task_5

nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]

def destructure(arr):
    res_list = []

    def traverse(arr):
        for item in arr:
            if isinstance(item, Iterable):
                traverse(item)
            else:
                res_list.append(item)

    traverse(arr)
    return res_list

print(destructure(nice_list))

# task_6

def quick_sort(arr):

    def _quick_sort(left_border, right_border):
        if right_border - left_border < 1:
            return
        
        left = left_border - 1
        for right in range(left_border, right_border + 1):
            if arr[right] <= arr[right_border]:
                left += 1
                if right > left:
                    arr[right], arr[left] = arr[left], arr[right]
        _quick_sort(left_border, left - 1)
        _quick_sort(left + 1, right_border)
        
    _quick_sort(0, len(arr) - 1)
    return arr