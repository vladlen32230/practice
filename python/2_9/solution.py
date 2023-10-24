import os

# task_1

with open('numbers.txt', 'r') as f:
    all_sum = 0

    for line in f.readlines():
        all_sum += int(line.strip())
    
    print(all_sum)

# task_2

with open('zen.txt', 'r') as f:
    print('\n'.join(reversed(f.readlines())))

# task_3

path = input('Введите путь: ')

files = os.listdir(path)
files_count = 0
files_size = 0
directories_count = 0

for file in files:
    full_path = os.path.join(path, file)
    if os.path.isfile(full_path):
        files_count += 1
        files_size += os.path.getsize(full_path)
    else:
        directories_count += 1

print(f'Размер каталога (в Кбайтах): {files_size / 1024}')
print(f'Количество подкаталогов: {directories_count}')
print(f'Количество файлов: {directories_count}')

# task_4

with open('first_tour.txt', 'r') as first_tour, open('second_tour.txt', 'w+') as second_tour:
    min_score = int(first_tour.readline())
    participants = []

    for participant in first_tour.readlines():
        name, surname, score = participant.split(' ')
        score = int(score)
        if score > min_score:
            participants.append( (name, surname, score) )

    participants.sort(key=lambda t: -t[2])
    
    second_tour.write(f'{len(participants)}')
    for place, participant in enumerate(participants):
        name, surname, score = participant
        second_tour.write(f'\n{place}) {surname[0]}. {name} {score}')

# task_5

with open('text.txt', 'r') as text, open('analysis.txt', 'w+') as analysis:
    freq = dict()

    for letter in text.readline().lower():
        if letter != ' ':
            if letter in freq:
                freq[letter] += 1
            else:
                freq[letter] = 1
    
    count = sum(freq.values())

    for letter, encounters in freq.items():
        analysis.write(f'{letter} {round(encounters / count, 3)}\n')

# task_6

# - нет материала для анализа, но оно очень похоже на 5 задание