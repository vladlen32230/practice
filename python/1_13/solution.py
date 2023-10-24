from sympy import Symbol, solve

# task_1

def to_float(num):
    if num >= 1:
        degree = 0
        while not (num < 10 and num >= 1):
            num /= 10
            degree += 1
        print(f'{num} * 10 ** {degree}')
    else:
        degree = 0
        while not (num < 10 and num >= 1):
            num *= 10
            degree += 1
        print(f'{num} * 10 ** -{degree}')

# task_2

def maximum_of_two(num_1, num_2):
    return max(num_1, num_2)

def maximum_of_three(num_1, num_2, num_3):
    return maximum_of_two(maximum_of_two(num_1, num_2), maximum_of_two(num_2, num_3))

# task_3

def reverse_num(num):
    num = str(num)
    return (num[::-1])

def sum_reverse():
    num_1 = int(input('Введите первое число: '))
    num_2 = int(input('Введите второе число: '))

    num_1_reverse = int(reverse_num(num_1))
    num_2_reverse = int(reverse_num(num_2))

    print(f'Первое число наоборот: {reverse_num(num_1)}')
    print(f'Второе число наоборот: {reverse_num(num_2)}')
    print(f'Сумма: {num_1_reverse + num_2_reverse}')
    print(f'Сумма наоборот: {reverse_num(num_1_reverse + num_2_reverse)}')

# task_4

def count_numbers(num):
    return len(str(num))

def change_number(num):
    return int(str(num)[-1] + str(num)[1:-1] + str(num)[0])

def main():
    num_1 = int(input("Введите первое число: "))

    digits_count_num_1 = count_numbers(num_1)
    if digits_count_num_1 < 3:
        print("В первом числе меньше трёх цифр.")
        return
    
    changed_num_1 = change_number(num_1)

    print(f'Измененное первое число: {changed_num_1}')

    num_2 = int(input("Введите первое число: "))

    digits_count_num_2 = count_numbers(num_2)
    if digits_count_num_2 < 4:
        print("Во втором числе меньше четырёх цифр.")
        return
    
    changed_num_2 = change_number(num_2)

    print(f'Измененное второе число: {changed_num_2}')

    print(f'Сумма чисел: {changed_num_1 + changed_num_2}')

# task_5

def count_swings():
    start_amp = float(input('Введите начальную амплитуду: '))
    end_amp = float(input('Введите амплитуду остановки: '))
    count = 0

    while start_amp > end_amp:
        start_amp *= 0.916
        count += 1
    
    print(f'Маятник считается остановившимся через {count} колебаний')

# task_6

x = Symbol('x')
expr = x ** 3 - 3 * x ** 2 - 12 * x + 10

roots = solve(expr)

print(f'Оптимальные глубины: {roots}')