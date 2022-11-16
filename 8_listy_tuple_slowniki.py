# #listy
# progr = ['PHP', 'Python']
# print(progr)

# progr.append('C#')
# print(progr)

# count = progr.count('Python')
# print(f'Python występuje {count} razy')

# #tuple

# str = ('Janusz', 'Anna')
# int = (1, 2, 3)

# print(int)

# test = (1)
# print(type(test))

# #wyszukiwanie

# if 2 in int:
#     print('istnieje')
# else:
#     print('nie istnieje')

# #slowniki
# person = {
#     'name' : 'Anna',
#     'surname' : 'Nowak'
# }

# print(person)
# print(type(person))
# print(person['name'])
# print(person.keys())


People = dict()

People['0'] = input("Podaj imie: ")
People['1'] = input("Podaj imie: ")
People['2'] = input("Podaj imie: ")

for key,value in People.items():
    count = int(key) + 1
    print(f'Imię{count}: {value}')