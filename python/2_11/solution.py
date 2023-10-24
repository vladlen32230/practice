import random

# task_1

class Warrior:
    health = 100

    def __init__(self, name) -> None:
        self.name = name

    def hit(self, enemy):
        enemy.health -= 20
        print(f'{self.name} атаковал {enemy.name}, оставшееся здоровье: {enemy.health}')

warrior_1 = Warrior('vlad')
warrior_2 = Warrior('tyler')

while True:
    attack = random.randint(1, 2)

    if attack == 1:
        warrior_1.hit(warrior_2)
        if warrior_2.health == 0:
            print(f'{warrior_1.name} победил {warrior_2.name}')
            break
    else:
        warrior_2.hit(warrior_1)
        if warrior_1.health == 0:
            print(f'{warrior_2.name} победил {warrior_1.name}')
            break

# task_2

class Student:
    def __init__(self, name, surname, group, grades) -> None:
        self.name = name
        self.surname = surname
        self.group = group
        self.grades = grades

students = [
    Student('vlad', 'kudrin', 'РИ-220914', [4, 3, 5, 4, 2]), 
    Student('tyler', 'durden', None, [5, 4, 3, 5, 2]), 
    Student('serega', 'pirat', 'KGU', [2, 4, 3, 3, 2])
]

students.sort(key=lambda student: sum(student.grades) / len(student.grades))

# task_3

class Parent:
    def __init__(self, name, age, kids) -> None:
        self.name = name
        self.age = age
        self.kids = list(filter(lambda kid: age - kid.age > 15, kids))

    def info(self):
        print(f'Я родитель {self.name}, мне {self.age} лет, мои дети: {", ".join(map(lambda kid: kid.name))}')

    def calm_down_child(self, kid):
        if kid in self.kids:
            kid.anxiety = False
        else:
            print('Это не мой ребенок')
    
    def feed_kid(self, kid):
        if kid in self.kids:
            kid.hunger = False
        else:
            print('Это не мой ребенок')

class Kid:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.anxiety = False
        self.hunger = False

# task_4

class Water:
    def __str__(self) -> str:
        return 'Water'
    
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        return None

class Air:
    def __str__(self) -> str:
        return 'Air'
    
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lighting()
        elif isinstance(other, Earth):
            return Dust()
        return None


class Fire:
    def __str__(self) -> str:
        return 'Fire'
    
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lighting()
        elif isinstance(other, Earth):
            return Lava()
        return None

class Earth:
    def __str__(self) -> str:
        return 'Earth'
    
    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        return None

class Storm:
    def __str__(self) -> str:
        return 'Storm'

class Steam:
    def __str__(self) -> str:
        return 'Steam'

class Dirt:
    def __str__(self) -> str:
        return 'Dirt'

class Lighting:
    def __str__(self) -> str:
        return 'Lighting'

class Dust:
    def __str__(self) -> str:
        return 'Dust'

class Lava:
    def __str__(self) -> str:
        return 'Lava'
    
# task_5

class Person:
    def __init__(self, name, house) -> None:
        self.name = name
        self.hunger = 50
        self.house = house
        self.dead = False

    def eat(self):
        if self.house.food < 10:
            print('Нет еды')
            if self.hunger <= 0:
                print(f'{self.name} умер от голода')
                self.dead = True
        else:
            self.hunger += 25
            self.house.food -= 5
            print(f'{self.name} поел')

    def work(self):
        self.hunger -= 15
        if self.hunger <= 0:
            print(f'{self.name} умер от голода')
            self.dead = True
        else:
            self.house.money += 30
            print(f'{self.name} поработал')
    
    def play(self):
        self.hunger -= 15
        if self.hunger <= 0:
            print(f'{self.name} умер от голода')
            self.dead = True
        else:
            print(f'{self.name} поиграл')
    
    def get_food(self):
        if self.house.money < 25:
            print(f'Нет денег на еду у {self.name}')
        else:
            self.house.money -= 25
            self.house.food += 50
            print(f'{self.name} купил еды')
        
    def live_day(self):
        num = random.randint(1, 6)
        self.hunger -= 5

        if self.hunger <= 20:
            self.eat()
        elif self.house.food < 10:
            self.get_food()
        elif self.house.money < 50 or num == 1:
            self.work()
        elif num == 2:
            self.eat
        else:
            self.play()

class Home:
    def __init__(self) -> None:
        self.food = 50
        self.money = 0

house = Home()
person_1 = Person('vlad', house)
person_2 = Person('tyler', house)

for _ in range(365):
    person_1.live_day()
    if person_1.dead:
        break

    person_2.live_day()
    if person_2.dead:
        break

# task_6

class Game:
    def __init__(self, player_1, player_2) -> None:
        self.player_1 = player_1
        self.player_2 = player_2
        self.board = None
        self.started = False
    
    def start_game(self):
        if not self.started:
            self.board = {i: i for i in range(1, 10)}

            rand = random.randint(0, 1)
            x = self.player_1 if rand else self.player_2
            o = self.player_1 if not rand else self.player_2

            self.view_board(x, o)

            for i in range(1, 10):
                if i % 2 == 1:
                    x.move(self)
                else:
                    o.move(self)
                
                self.view_board(x, o)

                winner = self.check_winner()
                if winner:
                    print(f'{winner.name} - победитель!')
                    winner.wins += 1
                    self.started = False
                    break
            else:
                print('Ничья!')
    
    def view_board(self, x, o):
        def parse_cell(cell):
            if self.board[cell] is x:
                return 'X'
            elif self.board[cell] is o:
                return 'O'
            return self.board[cell]

        print('Текущая доска: ')
        for row in range(3):
            print(f'[{parse_cell(row * 3 + 1)} {parse_cell(row * 3 + 2)} {parse_cell(row * 3 + 3)}]')
        
    def check_winner(self):
        def check(comb):
            if comb[0] is comb[1] and comb[1] is comb[2]:
                return comb[1]
            return None
        
        combinations = [
            [self.board[1], self.board[4], self.board[7]],
            [self.board[2], self.board[5], self.board[8]],
            [self.board[3], self.board[6], self.board[9]],
            [self.board[1], self.board[2], self.board[3]],
            [self.board[4], self.board[5], self.board[6]],
            [self.board[7], self.board[8], self.board[9]],
            [self.board[1], self.board[5], self.board[9]],
            [self.board[3], self.board[5], self.board[7]]
        ]

        for comb in combinations:
            winner = check(comb)
            if winner:
                return winner

        return None

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.wins = 0

    def move(self, game):
        while True:
            print(f'Ход {self.name}')
            cell = int(input('Введите клетку от 1 до 9: '))
            if isinstance(game.board[cell], Player):
                print('Эта клетка занята')
            else:
                game.board[cell] = self
                break



player_1 = Player('vlad')
player_2 = Player('tyler')

game = Game(player_1, player_2)

# task_7

class Matrix:
    def __init__(self, matrix) -> None:
        self.matrix = matrix

    def _add_or_sub(self, other, action):
        new_matrix = [[0 for cols in range(len(self.matrix[0]))] for rows in range(len(self.matrix))]

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if action == '+':
                    new_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
                elif action == '-':
                    new_matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
        
        return Matrix(new_matrix)

    def __add__(self, other):
        return self._add_or_sub(other, '+')
    
    def __sub__(self, other):
        return self._add_or_sub(other, '-')
    
    def __mul__(self, other):
        new_matrix = [[0 for cols in range(len(other.matrix[0]))] for rows in range(len(self.matrix))]

        for i in range(len(new_matrix)):
            for j in range(len(new_matrix[0])):
                row = self.matrix[i]
                col = [other.matrix[row][j] for row in range(len(other.matrix[0]))]
                multiplications = [row_cell * col_cell for row_cell, col_cell in zip(row, col)]
                new_matrix[i][j] = sum(multiplications)
    
        return Matrix(new_matrix)
    
    def T(self):
        new_matrix = [[0 for cols in range(len(self.matrix[0]))] for rows in range(len(self.matrix))]

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                new_matrix[i][j] = self.matrix[j][i]

        return Matrix(new_matrix)

matr = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print( (matr + matr).matrix )
print( (matr - matr).matrix )
print((matr * matr).matrix )
print(matr.T().matrix)