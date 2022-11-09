# slownik = {'klucz1': 'wartosc1', 'klucz2': 'wartosc2'}

# print(slownik)
# print(slownik['klucz1'])

# worker = {
#     'imie': 'Fryderyk',
#     'nazwisko': 'Bezrobotny',
#     'miasto': 'Poznań', 
#     'wiek': 50, 
#     'imiona_dzieci': ['Anna', 'Piotr'], 
#     'imiona_rodzicow': ['Jadwiga', 'Stefan']
#     }

# print(worker)
# print(worker['imiona_dzieci'])
# print(worker['imiona_dzieci'][0])

# worker['wzrost'] = 180

# print(worker)

# key = 'imie'

# if key in worker:
#     del worker[key]
#     print(f'klucz {key} został usunięty!')
# else:
#     print(f'klucz {key} nie został usunięty')

# print(worker)

wygrane = [4,48,23,41,30,27]

print('Podaj 6 liczb:')
lotto = {
    'num1' : input("Liczba 1: "),
    'num2' : input("Liczba 2: "),
    'num3' : input("Liczba 3: "),
    'num4' : input("Liczba 4: "),
    'num5' : input("Liczba 5: "),
    'num6' : input("Liczba 6: ")
}

for num in lotto:
    for traf in wygrane:
        if traf = lotto[num]:
            print('Wygrana')
