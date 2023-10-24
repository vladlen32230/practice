import random

# task_1

def summa_n(n):
    print(sum(range(1, n + 1)))

# task_2

def test():
    num = int(input('Введите число: '))
    if num > 0:
        def positive():
            print('Число положительное')
        positive()
    elif num < 0:
        def negative():
            print('Число отрицательное')
        negative()

# task_3

def calculator():
    def get_digits(num):
        res = []
        while num > 9:
            res.append(num % 10)
            num //= 10
        res.append(num)
        return res
    
    def sum_digits(num):
        return sum(get_digits(num))
    
    def max_digit(num):
        return max(get_digits(num))
    
    def min_digit(num):
        return min(get_digits(num))
        
    while True:
        num = int(input('Введите число: '))
        action = input('Введите действие (sum, max, min): ')
        
        if action == 'sum':
            print(sum_digits(num))
        elif action == 'max':
            print(max_digit(num))
        elif action == 'min':
            print(min_digit(num))
        else:
            break

# task_4

def reverse_num(num):
    num = str(num)
    print(num[::-1])

# task_5

def count_letters():
    text = input('Введите текст: ')
    digit = input('Какую цифру ищем? ')
    letter = input('Какую букву ищем? ')

    print(f'Количество цифр {digit}: {text.count(digit)}')
    print(f'Количество букв {letter}: {text.count(letter)}')

# task_6

def great_com_divisor(num_1, num_2):
    res = 1
    divisor = 2
    while divisor * 2 <= num_1 or divisor * 2 <= num_2:
        if num_1 % divisor == 0 and num_2 % divisor == 0:
            res *= divisor
            num_1 //= divisor
            num_2 //= divisor
            divisor = 2
        else:
            divisor += 1
    
    print(f'НОД: {res}')

# task_7

def rock_paper_scissors():
  rps = ['камень', 'ножницы', 'бумага']

  while True:
    computer = rps[random.randint(0, 2)]
    player = input('Введите камень, ножницы или бумага: ')

    if player == 'камень' and computer == 'ножницы' or player == 'ножницы' and computer == 'бумага' or player == 'бумага' and computer == 'камень':
        print(f'Вы выиграли! {player} выигрывает {computer}')
    elif computer == 'камень' and player == 'ножницы' or computer == 'ножницы' and player == 'бумага' or computer == 'бумага' and player == 'камень':
        print(f'Вы проиграли. {computer} выигрывает {player}')
    elif computer == player:
        print('Ничья')
    else:
        return

def guess_the_number():
    end = int(input('Введите число n (угадывать число от 1 до n): '))

    while True:
        number = random.randint(1, end)

        while True:
            try:
                player = int(input('Введите число: '))
            except ValueError:
                return
            if (player > number):
                print('Неверно, вы взяли большее число')
            elif player < number:
                print('Неверно, вы взяли меньшее число')
            else:
                print('Верно, вы выиграли!')

def mainMenu():
    while True:
        game = input('Введите игру: gtn (guess the number) или rcs (rock paper scissors)')
        if game == 'gtn':
            guess_the_number()
        elif game == 'rcs':
            rock_paper_scissors()
        else:
            return

mainMenu()