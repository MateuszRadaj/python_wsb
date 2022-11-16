slownik = {'klucz1': 'wartosc1', 'klucz2': 'wartosc2'}

print(slownik)
print(slownik['klucz1'])

worker = {
    'imie': 'Fryderyk',
    'nazwisko': 'Bezrobotny',
    'miasto': 'Poznań', 
    'wiek': 50, 
    'imiona_dzieci': ['Anna', 'Piotr'], 
    'imiona_rodzicow': ['Jadwiga', 'Stefan']
    }

print(worker)
print(worker['imiona_dzieci'])
print(worker['imiona_dzieci'][0])

worker['wzrost'] = 180

print(worker)

key = 'imie'

if key in worker:
    del worker[key]
    print(f'klucz {key} został usunięty!')
else:
    print(f'klucz {key} nie został usunięty')

print(worker)
print(worker.values())
print(worker.items())

print('\n###############################')

for value in worker.values():
    print(value, end=" ")

print('\n###############################')

for key, value in worker.items():
    print(f'{key}:{value}')