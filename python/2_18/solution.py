import re
import string
import requests
import json

# task_1

text = """ Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes,
nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. 
Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate 
"""

res = [word for word in re.sub(r'['+string.punctuation+']', '', text).split() if re.match(r'^[A-Z|a-z]{4}$', word)]

# task_2

numbers = 'А578ВЕ7777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'.split(' ')
letters = 'АВЕКМНОРСТУХ'

private = [number for number in numbers if re.match(r'^[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}(\d{3}|\d{2})$', number)]
taxi = [number for number in numbers if re.match(r'^[АВЕКМНОРСТУХ]{2}\d{3}(\d{2}|\d{3})$', number)]

print(private)
print(taxi)

# task_3

js = json.loads(requests.get('https://swapi.dev/api/starships/').content)['results']
ship_attributes = ['max_atmospheric_speed', 'ship_name', 'starship_class']
pilot_attributes = ['height', 'homeworld', 'homeworld_url', 'mass', 'name']

for ship in js:
    if ship['name'] == 'Millennium Falcon':
        info = {k: v for k, v in ship.items() if k in ship_attributes}
        info['pilots'] = []
        for pilot_url in ship['pilots']:
            pilot = json.loads(requests.get(pilot_url).content)
            info['pilots'].append({k: v for k, v in pilot.items() if k in pilot_attributes})
        with open('json.json', 'w+') as f:
            json.dump(info, f, indent=4)
        break

# task_4

numbers = ['9999999999', '999999-999', '99999x9999']

for index, number in enumerate(numbers, 1):
    if re.match(r'^[8-9]\d{9}$', number):
        print(f'{index} номер: всё в порядке')
    else:
        print(f'{index} номер: не подходит')

# task_5

html = str(requests.get('http://www.columbia.edu/~fdc/sample.html').content)
headers = re.findall(r'<h3.*?>(.*?)</h3>', html)

# task_6

# no materials