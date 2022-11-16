# def show():
#     print('Witaj', end=' ')
#     print('Anna')

# show()

# def iloraz(a, b):
#     return a/b

# print(iloraz(2,3))
# print(iloraz(9,2))

def przypisz(marka,model,pojemnosc,pred_max):
    Car = {
        'marka' : marka,
        'model' : model,
        'pojemnosc' : pojemnosc,
        'pred_max' : pred_max
    }
    return Car

def wyswietl(car):
    for key in car:
        print('Marka: ' car[key])

marka = input('Podaj marke: ')
model = input('Podaj model: ')
pojemnosc = input('Podaj pojemnosc: ')
pred_max = input('Podaj predkosc maksymalna: ')

Car = przypisz(marka,model,pojemnosc,pred_max)

wyswietl(Car)